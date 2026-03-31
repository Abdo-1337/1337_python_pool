from ex0.Card import Card
from enum import Enum
from typing import Dict


class CreatureType(Enum):
    """Predefined creature card names."""

    FIRE_DRAGON = "Fire Dragon"
    GOBLIN_WARRIOR = "Goblin Warrior"
    ICE_WIZARD = "Ice Wizard"
    LIGHTNING_ELEMENTAL = "Lightning Elemental"
    STONE_GOLEM = "Stone Golem"
    SHADOW_ASSASSIN = "Shadow Assassin"
    HEALING_ANGEL = "Healing Angel"
    FOREST_SPRITE = "Forest Sprite"


class CreatureCard(Card):
    """Concrete card representing a creature with attack and health."""

    def __init__(
        self, name: str, cost: int, rarity: str, attack: int, health: int
    ) -> None:
        """Initialize a creature card with combat stats."""
        super().__init__(name, cost, rarity)
        if not isinstance(attack, int) or attack <= 0:
            raise ValueError("Attack value should be a positive integer")
        if not isinstance(health, int) or health <= 0:
            raise ValueError("Health value should be a positive integer")
        self.attack: int = attack
        self.health: int = health

    def play(self, game_state: Dict) -> Dict:
        """Summon the creature to the battlefield."""
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Creature summoned to battlefield",
        }

    def attack_target(self, target: str) -> Dict:
        """Attack a target and deal damage."""
        return {
            "attacker": self.name,
            "target": target,
            "damage_dealt": self.attack,
            "combat_resolved": True,
        }

    def get_card_info(self) -> Dict:
        """Return extended creature card information."""
        card_info = super().get_card_info()
        card_info["type"] = "Creature"
        card_info["attack"] = self.attack
        card_info["health"] = self.health

        return card_info
