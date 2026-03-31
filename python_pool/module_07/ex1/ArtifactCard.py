from ex0.Card import Card
from enum import Enum
from typing import Dict


class ArtifactType(Enum):
    """Predefined artifact card names."""

    MANA_CRYSTAL = "Mana Crystal"
    SWORD_OF_POWER = "Sword of Power"
    RING_OF_WISDOM = "Ring of Wisdom"
    SHIELD_OF_DEFENSE = "Shield of Defense"
    CROWN_OF_KINGS = "Crown of Kings"
    BOOTS_OF_SPEED = "Boots of Speed"
    CLOAK_OF_SHADOWS = "Cloak of Shadows"
    STAFF_OF_ELEMENTS = "Staff of Elements"


class ArtifactCard(Card):
    """Concrete card representing a permanent artifact."""

    def __init__(
            self,
            name: str,
            cost: int,
            rarity: str,
            durability: int,
            effect: str
            ) -> None:
        """Create an artifact card with durability and a special effect."""
        super().__init__(name, cost, rarity)
        if not isinstance(durability, int) or durability <= 0:
            raise ValueError("Durablity should be a positive integer")

        self.durability: int = durability
        self.effect: str = effect

    def play(self, game_state: Dict) -> Dict:
        """Place the artifact into play as a permanent effect."""
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": self.effect,
        }

    def activate_ability(self) -> Dict:
        """Activate the artifact's ongoing ability."""
        return {
            "artifact": self.name,
            "effect": self.effect,
            "durability_remaining": self.durability
        }

    def get_card_info(self) -> Dict:
        """Return artifact information including durability and effect."""
        info = super().get_card_info()
        info["type"] = "Artifact"
        info["durability"] = self.durability
        info["effect"] = self.effect
        return info
