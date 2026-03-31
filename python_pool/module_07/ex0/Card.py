from abc import ABC, abstractmethod
from typing import Dict


class Card(ABC):
    """Base abstract class for all cards in the DataDeck system."""

    def __init__(self, name: str, cost: int, rarity: str) -> None:
        """Create a card with a name, mana cost, and rarity."""
        self.name: str = name
        self.cost: int = cost
        self.rarity: str = rarity

    @abstractmethod
    def play(self, game_state: Dict) -> Dict:
        """Apply the card effect to the current game state."""
        pass

    def get_card_info(self) -> Dict:
        """Return the basic information describing the card."""
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity
            }

    def is_playable(self, available_mana: int) -> bool:
        """Check if the player has enough mana to play the card."""
        return available_mana >= self.cost
