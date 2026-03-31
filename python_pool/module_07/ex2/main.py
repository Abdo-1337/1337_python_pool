from ex2.EliteCard import EliteCard, SpellName
from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical
from typing import List


def get_class_methods(cls) -> List:
    """Return public method names defined in a class."""
    methods: List = []
    for key, value in cls.__dict__.items():
        if callable(value) and not key.startswith("_"):
            methods.append(key)
    return methods


def data_deck_ability() -> None:
    """Demonstrate multiple interface abilities of EliteCard."""

    print("EliteCard capabilities:")
    print("- Card:", get_class_methods(Card))
    print("- Combatable:", get_class_methods(Combatable))
    print("- Magical:", get_class_methods(Magical))

    arcane_warrior = EliteCard("Arcane Warrior", 6, "Epic", 5, 3, 10, 4, 4)
    print("Playing Arcane Warrior (Elite Card):")
    print()

    enemy = EliteCard("Enemy", 5, "Rare", 4, 2, 8, 3, 3)
    print("Combat phase:")
    print("Attack result:", arcane_warrior.attack(enemy))
    print("Defense result:", arcane_warrior.defend(5))
    print()

    print("Magic phase:")
    enemy_list = ["Enemy1", "Enemy2"]
    print("Spell cast:", arcane_warrior.cast_spell(
        SpellName.FIREBALL, enemy_list))
    print("Mana channel:", arcane_warrior.channel_mana(3))
    print()

    print("Multiple interface implementation successful!")


def main() -> None:
    """Entry point for the Ability System demonstration."""

    print("=== DataDeck Ability System ===")
    print()

    data_deck_ability()


if __name__ == "__main__":
    main()
