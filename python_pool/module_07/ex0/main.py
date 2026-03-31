from ex0.CreatureCard import CreatureCard


def ft_abc_design_test() -> None:
    """Run a simple demonstration of the CreatureCard behavior."""

    fire_dragon = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)

    print("CreatureCard Info:")
    print(fire_dragon.get_card_info())
    print()

    print("Playing Fire Dragon with 6 mana available:")
    print("Playable:", fire_dragon.is_playable(6))
    print("Play result:", fire_dragon.play({}))
    print()

    print("Fire Dragon attacks Goblin Warrior:")
    print("Attack result:", fire_dragon.attack_target("Goblin Warrior"))
    print()

    print("Testing insufficient mana (3 available):")
    print("Playable:", fire_dragon.is_playable(3))


def main() -> None:
    """Entry point for the Card Foundation demonstration."""

    print("=== DataDeck Card Foundation ===")
    print()

    print("Testing Abstract Base Class Design:")
    print()

    ft_abc_design_test()
    print()

    print("Abstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
