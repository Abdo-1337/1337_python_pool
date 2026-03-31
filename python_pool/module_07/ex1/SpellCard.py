from ex0.Card import Card
from enum import Enum
from typing import Dict


class SpellType(Enum):
    """Predefined spell card names."""

    LIGHTNING_BOLT = "Lightning Bolt"
    HEALING_POTION = "Healing Potion"
    FIREBALL = "Fireball"
    SHIELD_SPELL = "Shield Spell"
    METEOR = "Meteor"
    ICE_SHARD = "Ice Shard"
    DIVINE_LIGHT = "Divine Light"
    MAGIC_MISSILE = "Magic Missile"


class SpellCard(Card):
    """Concrete card representing a one-time spell effect."""

    def __init__(
            self,
            name: str,
            cost: int,
            rarity: str,
            effect_type: str
            ) -> None:
        """Create a spell card with a specific effect."""
        super().__init__(name, cost, rarity)
        self.effect_type: str = effect_type

    def play(self, game_state: Dict) -> Dict:
        """Cast the spell."""
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": self.effect_type
        }

    def resolve_effect(self, targets: list[str]) -> Dict:
        """Resolve the spell effect on the given targets."""
        return {
            "spell": self.name,
            "effect_type": self.effect_type,
            "targets": targets,
            "resolved": True
        }

    def get_card_info(self) -> Dict:
        """Return spell card information."""
        info = super().get_card_info()
        info["type"] = "Spell"
        info["effect_type"] = self.effect_type
        return info
