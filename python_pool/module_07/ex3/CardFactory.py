from abc import ABC, abstractmethod
from typing import Dict
from ex0.Card import Card


class CardFactory(ABC):
    """Abstract factory responsible for creating different card types."""

    @abstractmethod
    def create_creature(
        self,
        name_or_power: str | int | None = None
            ) -> Card:
        """Create and return a creature card."""
        pass

    @abstractmethod
    def create_spell(
        self,
        name_or_power: str | int | None = None
            ) -> Card:
        """Create and return a spell card."""
        pass

    @abstractmethod
    def create_artifact(
        self,
        name_or_power: str | int | None = None
            ) -> Card:
        """Create and return an artifact card."""
        pass

    @abstractmethod
    def create_themed_deck(
        self,
        size: int
            ) -> Dict:
        """Create a themed deck of cards."""
        pass

    @abstractmethod
    def get_supported_types(self) -> Dict:
        """Return the supported card types of the factory."""
        pass
