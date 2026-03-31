from ex3.CardFactory import CardFactory
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from typing import List, Dict
import random


class FantasyCardFactory(CardFactory):
    """Concrete factory that creates fantasy-themed cards."""

    _creatures: List = [
            {"name": "Fire Dragon", "cost": 5,
             "rarity": "Legendary", "attack": 7, "health": 5},
            {"name": "Goblin Warrior", "cost": 2,
             "rarity": "Common", "attack": 2, "health": 1},
            {"name": "Ice Wizard", "cost": 4,
             "rarity": "Rare", "attack": 3, "health": 4},
            {"name": "Lightning Elemental", "cost": 3,
             "rarity": "Uncommon", "attack": 4, "health": 2},
            {"name": "Stone Golem", "cost": 6,
             "rarity": "Rare", "attack": 5, "health": 8},
            {"name": "Shadow Assassin", "cost": 3,
             "rarity": "Uncommon", "attack": 5, "health": 2},
            {"name": "Healing Angel", "cost": 4,
             "rarity": "Rare", "attack": 2, "health": 6},
            {"name": "Forest Sprite", "cost": 1,
             "rarity": "Common", "attack": 1, "health": 1},
        ]
    _spells: List = [
            {"name": "Lightning Bolt", "cost": 3,
             "rarity": "Common", "effect_type": "damage"},
            {"name": "Healing Potion", "cost": 2,
             "rarity": "Common", "effect_type": "heal"},
            {"name": "Fireball", "cost": 4,
             "rarity": "Uncommon", "effect_type": "damage"},
            {"name": "Shield Spell", "cost": 1,
             "rarity": "Common", "effect_type": "buff"},
            {"name": "Meteor", "cost": 8,
             "rarity": "Legendary", "effect_type": "damage"},
            {"name": "Ice Shard", "cost": 2,
             "rarity": "Common", "effect_type": "damage"},
            {"name": "Divine Light", "cost": 5,
             "rarity": "Rare", "effect_type": "heal"},
            {"name": "Magic Missile", "cost": 1,
             "rarity": "Common", "effect_type": "damage"},
        ]
    _artifacts: List = [
            {"name": "Mana Crystal", "cost": 2, "rarity": "Common",
             "durability": 5, "effect": "Permanent: +1 mana per turn"},
            {"name": "Sword of Power", "cost": 3, "rarity": "Uncommon",
             "durability": 3,
             "effect": "Permanent: +2 attack to equipped creature"},
            {"name": "Ring of Wisdom", "cost": 4, "rarity": "Rare",
             "durability": 4,
             "effect": "Permanent: Draw an extra card each turn"},
            {"name": "Shield of Defense", "cost": 5, "rarity": "Rare",
             "durability": 6,
             "effect": "Permanent: +3 health to all friendly creatures"},
            {"name": "Crown of Kings", "cost": 7, "rarity": "Legendary",
             "durability": 8,
             "effect": "Permanent: +1 cost reduction to all cards"},
            {"name": "Boots of Speed", "cost": 2, "rarity": "Uncommon",
             "durability": 2, "effect": "Permanent: Cards cost 1 less mana"},
            {"name": "Cloak of Shadows", "cost": 3, "rarity": "Uncommon",
             "durability": 3, "effect": "Permanent: Creatures have stealth"},
            {"name": "Staff of Elements", "cost": 6, "rarity": "Legendary",
             "durability": 7, "effect": "Permanent: +1 spell damage"},
        ]

    def create_creature(
        self,
        name_or_power: str | int | None = None
            ) -> CreatureCard:
        """Create a creature card based on a name or cost preference."""
        if isinstance(name_or_power, str):
            for creature in self._creatures:
                if name_or_power in creature["name"]:
                    return CreatureCard(**creature)
            return CreatureCard(**random.choice(self._creatures))

        if isinstance(name_or_power, int):
            for creature in self._creatures:
                if name_or_power == creature["cost"]:
                    return CreatureCard(**creature)
            for creature in self._creatures:
                if name_or_power == creature["cost"] + 1:
                    return CreatureCard(**creature)
            for creature in self._creatures:
                if name_or_power == creature["cost"] - 1:
                    return CreatureCard(**creature)
            return CreatureCard(**random.choice(self._creatures))

        return CreatureCard(**random.choice(self._creatures))

    def create_spell(
        self,
        name_or_power: str | int | None = None
            ) -> SpellCard:
        """Create a spell card based on a name or cost preference."""
        if isinstance(name_or_power, str):
            for spell in self._spells:
                if name_or_power in spell["name"]:
                    return SpellCard(**spell)
            return SpellCard(**random.choice(self._spells))

        if isinstance(name_or_power, int):
            for spell in self._spells:
                if name_or_power == spell["cost"]:
                    return SpellCard(**spell)

            for spell in self._spells:
                if name_or_power == spell["cost"] + 1:
                    return SpellCard(**spell)

            for spell in self._spells:
                if name_or_power == spell["cost"] - 1:
                    return SpellCard(**spell)

            return SpellCard(**random.choice(self._spells))

        return SpellCard(**random.choice(self._spells))

    def create_artifact(
        self,
        name_or_power: str | int | None = None
            ) -> ArtifactCard:
        """Create an artifact card based on a name or cost preference."""
        if isinstance(name_or_power, str):
            for artifact in self._artifacts:
                if name_or_power in artifact["name"]:
                    return ArtifactCard(**artifact)
            return ArtifactCard(**random.choice(self._artifacts))

        if isinstance(name_or_power, int):
            for artifact in self._artifacts:
                if name_or_power == artifact["cost"]:
                    return ArtifactCard(**artifact)

            for artifact in self._artifacts:
                if name_or_power == artifact["cost"] + 1:
                    return ArtifactCard(**artifact)

            for artifact in self._artifacts:
                if name_or_power == artifact["cost"] - 1:
                    return ArtifactCard(**artifact)

            return ArtifactCard(**random.choice(self._artifacts))

        return ArtifactCard(**random.choice(self._artifacts))

    def create_themed_deck(
        self,
        size: int
            ) -> Dict:
        """Generate a randomized fantasy-themed deck of cards."""
        cards_created: List[Card] = []
        for _ in range(size):
            card_type = random.choice(["creature", "artifact", "spell"])

            if card_type == "creature":
                cards_created.append(self.create_creature())

            elif card_type == "spell":
                cards_created.append(self.create_spell())

            else:
                cards_created.append(self.create_artifact())

        return {
            "deck_size": len(cards_created),
            "cards": cards_created
        }

    def get_supported_types(self) -> Dict[str, List[str]]:
        """
        Return the creature, spell,
        and artifact types supported by this factory.
        """
        return {
            "creatures": ["dragon", "goblin"],
            "spells": ["fireball"],
            "artifacts": ["mana_ring"]
            }
