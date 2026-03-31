from datetime import datetime
from enum import Enum
from typing import Any, Dict, List

from pydantic import BaseModel, Field, ValidationError, model_validator


class Rank(str, Enum):
    """Crew member rank."""

    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):
    """
    Crew member with rank, role, and experience.
    """

    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    """
    Space mission containing crew and validation rules.
    """

    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: List[CrewMember]
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def validate_mission(self) -> "SpaceMission":
        """
        Validate mission-level rules across crew and duration.
        """
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")

        if not any(
            member.rank in (Rank.commander, Rank.captain)
            for member in self.crew
        ):
            raise ValueError(
                "Mission must have at least one Commander or Captain"
            )

        if self.duration_days > 365:
            experienced = sum(
                member.years_experience >= 5 for member in self.crew
            )
            if experienced < len(self.crew) / 2:
                raise ValueError(
                    "Long missions require at least 50% experienced crew"
                )

        if not all(member.is_active for member in self.crew):
            raise ValueError("All crew members must be active")

        return self


def process_mission(data: Dict[str, Any]) -> None:
    """
    Create a SpaceMission and print result or validation error.
    """
    try:
        mission = SpaceMission(**data)

        print("Valid mission created:")
        print(f"Mission: {mission.mission_name}")
        print(f"ID: {mission.mission_id}")
        print(f"Destination: {mission.destination}")
        print(f"Duration: {mission.duration_days} days")
        print(f"Budget: ${mission.budget_millions}M")
        print(f"Crew size: {len(mission.crew)}")

        print("Crew members:")
        for member in mission.crew:
            print(
                f"- {member.name} ({member.rank.value}) - "
                f"{member.specialization}"
            )

    except ValidationError as e:
        print("Expected validation error:")
        print(e.errors()[0]["msg"].split(", ")[1])


def main() -> None:
    """
    Run examples with valid and invalid mission data.
    """
    print("Space Mission Crew Validation")
    print("=" * 41)

    valid_data = {
        "mission_id": "M2024_MARS",
        "mission_name": "Mars Colony Establishment",
        "destination": "Mars",
        "launch_date": "2026-03-31T10:30:00",
        "duration_days": 900,
        "budget_millions": 2500.0,
        "crew": [
            {
                "member_id": "C001",
                "name": "Sarah Connor",
                "rank": "commander",
                "age": 45,
                "specialization": "Mission Command",
                "years_experience": 15,
            },
            {
                "member_id": "C002",
                "name": "John Smith",
                "rank": "lieutenant",
                "age": 34,
                "specialization": "Navigation",
                "years_experience": 6,
            },
            {
                "member_id": "C003",
                "name": "Alice Johnson",
                "rank": "officer",
                "age": 29,
                "specialization": "Engineering",
                "years_experience": 5,
            },
        ],
    }

    invalid_data = {
        "mission_id": "M2024_FAIL",
        "mission_name": "Test Mission",
        "destination": "Mars",
        "launch_date": "2026-03-31T10:30:00",
        "duration_days": 100,
        "budget_millions": 500.0,
        "crew": [
            {
                "member_id": "C004",
                "name": "Bob Brown",
                "rank": "officer",
                "age": 30,
                "specialization": "Engineering",
                "years_experience": 3,
            }
        ],
    }

    process_mission(valid_data)

    print()
    print("=" * 41)

    process_mission(invalid_data)


if __name__ == "__main__":
    main()
