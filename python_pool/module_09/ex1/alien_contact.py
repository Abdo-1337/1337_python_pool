from datetime import datetime
from enum import Enum
from typing import Any, Dict, Optional

from pydantic import BaseModel, Field, ValidationError, model_validator


class ContactType(str, Enum):
    """Type of alien contact."""

    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"


class AlienContact(BaseModel):
    """
    Alien contact report with validation rules.
    """

    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = False

    @model_validator(mode="after")
    def validate_business_rules(self) -> "AlienContact":
        """
        Apply cross-field validation rules.
        """
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with 'AC'")

        if (
            self.contact_type == ContactType.physical
            and not self.is_verified
        ):
            raise ValueError("Physical contact reports must be verified")

        if (
            self.contact_type == ContactType.telepathic
            and self.witness_count < 3
        ):
            raise ValueError(
                "Telepathic contact requires at least 3 witnesses"
            )

        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError("Strong signals must include a message")

        return self


def process_contact(data: Dict[str, Any]) -> None:
    """
    Create an AlienContact and print result or validation error.
    """
    try:
        contact = AlienContact(**data)

        print("Valid contact report:")
        print(f"ID: {contact.contact_id}")
        print(f"Type: {contact.contact_type.value}")
        print(f"Location: {contact.location}")
        print(f"Signal: {contact.signal_strength}/10")
        print(f"Duration: {contact.duration_minutes} minutes")
        print(f"Witnesses: {contact.witness_count}")

        if contact.message_received:
            print(f"Message: '{contact.message_received}'")

    except ValidationError as e:
        print("Expected validation error:")
        print(e.errors()[0]["msg"].split(", ")[1])


def main() -> None:
    """
    Run examples with valid and invalid contact data.
    """
    print("Alien Contact Log Validation")
    print("=" * 38)

    valid_data = {
        "contact_id": "AC_2024_001",
        "timestamp": "2026-03-31T10:30:00",
        "location": "Area 51, Nevada",
        "contact_type": "radio",
        "signal_strength": 8.5,
        "duration_minutes": 45,
        "witness_count": 5,
        "message_received": "Greetings from Zeta Reticuli",
    }

    invalid_data = {
        "contact_id": "AC_2024_002",
        "timestamp": "2026-03-31T10:30:00",
        "location": "Unknown Sector",
        "contact_type": "telepathic",
        "signal_strength": 5.0,
        "duration_minutes": 30,
        "witness_count": 1,
    }

    process_contact(valid_data)

    print()
    print("=" * 38)

    process_contact(invalid_data)


if __name__ == "__main__":
    main()
