from abc import ABC, abstractmethod
from ex0.Card import Card
from typing import Dict


class Combatable(ABC):
    """Interface defining combat capabilities for cards."""

    @abstractmethod
    def attack(self, target: Card) -> Dict:
        """Attack a target card."""
        pass

    @abstractmethod
    def defend(self, incoming_damage: int) -> Dict:
        """Defend against incoming damage."""
        pass

    @abstractmethod
    def get_combat_stats(self) -> Dict:
        """Return combat-related statistics."""
        pass
