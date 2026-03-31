from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from ex0.CreatureCard import CreatureCard
from ex1.Deck import Deck


def ft_data_deck_builder() -> None:
    """Demonstrate deck creation and polymorphic card usage."""

    data_deck = Deck()

    lightning_bolt = SpellCard(
        "Lightning Bolt",
        3,
        "Uncommon",
        "Deal 3 damage to target"
        )
    mana_crystal = ArtifactCard(
        "Mana Crystal",
        4,
        "Common",
        3,
        "Permanent: +1 mana per turn"
    )
    fire_dragon = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)

    data_deck.add_card(lightning_bolt)
    data_deck.add_card(mana_crystal)
    data_deck.add_card(fire_dragon)

    print("Building deck with different card types...")
    print("Deck stats:", data_deck.get_deck_stats())
    print()

    print("Drawing and playing cards:")
    print()

    while data_deck.cards:
        card = data_deck.draw_card()
        card_type = card.get_card_info().get("type")

        print(f"Drew: {card.name} ({card_type})")
        print(f"Play result: {card.play({})}")
        print()

    print("Polymorphism in action: Same interface, different card behaviors!")


def main() -> None:
    """Entry point for the Deck Builder demonstration."""

    print("=== DataDeck Deck Builder ===")
    print()

    ft_data_deck_builder()


if __name__ == "__main__":
    main()
