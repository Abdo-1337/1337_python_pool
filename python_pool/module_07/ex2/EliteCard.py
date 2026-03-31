from ex2.Combatable import Combatable
from ex2.Magical import Magical
from ex0.Card import Card
import random
from enum import Enum
from typing import Dict, List


class SpellName(Enum):
    FIREBALL = "Fireball"
    LIGHTNING = "Lightning"
    ICE_BLAST = "Ice Blast"
    ARCANE_WAVE = "Arcane Wave"


class EliteCard(Card, Combatable, Magical):
    """Card with both combat and magical abilities."""

    def __init__(
            self,
            name: str,
            cost: int,
            rarity: str,
            attack_power: int,
            defense: int,
            health: int,
            mana: int,
            spell_power: int
            ) -> None:
        """Initialize an elite card with combat and magic stats."""
        super().__init__(name, cost, rarity)
        self.attack_power: int = attack_power
        self.defense: int = defense
        self.health: int = health
        self.mana: int = mana
        self.spell_power: int = spell_power

    def play(self, game_state: Dict) -> Dict:
        """Play the elite card."""
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Elite warrior enters with combat and magic"
        }

    def attack(self, target: Card) -> Dict:
        """Attack another card."""
        return {
            "attacker": self.name,
            "target": target.name,
            "damage": self.attack_power,
            "combat_type": "melee"
        }

    def defend(self, incoming_damage: int) -> Dict:
        """Defend against an incoming attack."""
        damage_taken = incoming_damage - self.defense
        if damage_taken < 0:
            damage_taken = 0
        return {
            "defender": self.name,
            "damage_taken": damage_taken,
            "damage_blocked": self.defense,
            "still_alive": (self.health - damage_taken) > 0
        }

    def cast_spell(self, spell_name: SpellName, targets: List) -> Dict:
        """Cast a spell on targets."""
        mana_used = random.randint(2, 5)

        return {
            "caster": self.name,
            "spell": spell_name.value,
            "targets": targets,
            "mana_used": mana_used
        }

    def channel_mana(self, amount: int) -> Dict:
        """Increase available mana."""
        self.mana += amount
        return {
            "channeled": amount,
            "total_mana": self.mana
        }

    def get_combat_stats(self) -> Dict:
        """Return combat statistics."""
        return {
            "attack": self.attack_power,
            "defense": self.defense,
            "health": self.health
        }

    def get_magic_stats(self) -> Dict:
        """Return magic statistics."""
        return {
            "mana": self.mana,
            "spell_power": self.spell_power
        }
