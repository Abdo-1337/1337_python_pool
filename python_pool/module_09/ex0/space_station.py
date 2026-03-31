from pydantic import BaseModel, Field, ValidationError
from datetime import datetime
from typing import Optional, Any, Dict


class SpaceStation(BaseModel):
    """
    Represents a space station and validates its data.

    Ensures values like crew size, power, and oxygen stay within limits.
    """

    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: Optional[str] = Field(default=None, max_length=200)


def process_station(data: Dict[str, Any]) -> None:
    """
    Create a SpaceStation from input data.

    Prints the station info if valid,
    otherwise prints the validation error.
    """
    try:
        station = SpaceStation(**data)

        print("Valid station created:")
        print(f"ID: {station.station_id}")
        print(f"Name: {station.name}")
        print(f"Crew: {station.crew_size} people")
        print(f"Power: {station.power_level}%")
        print(f"Oxygen: {station.oxygen_level}%")
        print(
            f"Status: {'Operational' if station.is_operational else 'Offline'}"
        )

    except ValidationError as e:
        print("Expected validation error:")
        print(e.errors()[0]["msg"])


def main() -> None:
    """
    Run examples with valid and invalid station data.
    """

    print("Space Station Data Validation")
    print("=" * 40)

    valid_data = {
        "station_id": "ISS001",
        "name": "International Space Station",
        "crew_size": 6,
        "power_level": 85.5,
        "oxygen_level": 92.3,
        "last_maintenance": "2024-03-20T10:30:00",
    }

    invalid_data = {
        "station_id": "BAD001",
        "name": "Broken Station",
        "crew_size": 25,
        "power_level": 50.0,
        "oxygen_level": 50.0,
        "last_maintenance": "2024-03-20T10:30:00",
    }

    process_station(valid_data)

    print()
    print("=" * 40)

    process_station(invalid_data)


if __name__ == "__main__":
    main()
