from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def ft_data_deck_platform() -> None:
    print("Registering Tournament Cards...")

    card_1 = TournamentCard("Fire Dragon", 5, "Legendary", 9, 7, 5, 1200)
    card_2 = TournamentCard("Ice Wizard", 4, "Rare", 6, 4, 3, 1150)

    tournament = TournamentPlatform()
    card1_id = tournament.register_card(card_1)
    card2_id = tournament.register_card(card_2)

    print(f"{card_1.name} (ID: {card1_id}):")
    print("- Interfaces: [Card, Combatable, Rankable]")
    print(f"- Rating: {card_1.rating}")
    print(f"- Record: {card_1.wins}-{card_1.losses}")
    print()

    print(f"{card_2.name} (ID: {card2_id}):")
    print("- Interfaces: [Card, Combatable, Rankable]")
    print(f"- Rating: {card_2.rating}")
    print(f"- Record: {card_2.wins}-{card_2.losses}")
    print()

    print("Creating tournament match...")

    match_result = tournament.create_match(card1_id, card2_id)
    match_result.pop("comment", None)

    print("Match result:", match_result)
    print()

    print("Tournament Leaderboard:")

    leaderboard = tournament.get_leaderboard()

    for line in leaderboard:
        print(line)

    print()
    print("Platform Report:")
    print(tournament.generate_tournament_report())
    print()


def main() -> None:
    print("=== DataDeck Tournament Platform ===")
    print()

    ft_data_deck_platform()

    print()
    print("=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    main()
