from ex4.TournamentCard import TournamentCard
from typing import Dict, List
from enum import Enum
import random


class PlatformStatus(Enum):
    ACTIVE = "active"
    DESACTIVE = "desactive"


class TournamentPlatform:
    """Platform that manages tournament cards and match results."""
    def __init__(self):
        """Initialize the tournament platform."""
        self.cards: Dict[str, TournamentCard] = {}
        self.matches_played: int = 0

    def register_card(self, card: TournamentCard) -> str:
        """Register a tournament card and return its unique ID."""

        card_type = card.name.split()[-1].lower()

        count = 0
        for name in self.cards:
            if name.startswith(card_type):
                count += 1
        count += 1

        number = f"{count:03}"

        card_id = f"{card_type}_{number}"

        self.cards[card_id] = card

        return card_id

    def create_match(self, card1_id: str, card2_id: str) -> Dict:
        """Create a match between two cards and update rankings."""

        card1 = self.cards[card1_id]
        card2 = self.cards[card2_id]

        if card1.attack_power >= card2.attack_power:
            winner = card1
            loser = card2
            winner_id = card1_id
            loser_id = card2_id
        else:
            winner = card2
            loser = card1
            winner_id = card2_id
            loser_id = card1_id

        winner.update_wins(1)
        winner_rating = winner.calculate_rating()

        loser.update_losses(1)
        loser_rating = loser.calculate_rating()

        self.matches_played += 1
        commentary = random.choice([
            "A fierce battle!",
            "A quick victory!",
            "An intense duel!"
            ])

        return {
            "winner": winner_id,
            "loser": loser_id,
            "winner_rating": winner_rating,
            "loser_rating": loser_rating,
            "comment": commentary
        }

    def get_leaderboard(self) -> List:
        """Return a sorted leaderboard based on card ratings."""

        cards = list(self.cards.values())

        swaped = True
        while swaped:
            swaped = False
            for i in range(len(cards) - 1):
                if cards[i].rating <= cards[i + 1].rating:
                    cards[i], cards[i + 1] = (cards[i + 1], cards[i])
                    swaped = True

        leaderboard = []

        rank = 1
        for card in cards:
            leaderboard.append(
                f"{rank}. {card.name} - Rating: {card.rating}"
                f" ({card.wins}-{card.losses})"
                    )

        return leaderboard

    def generate_tournament_report(self) -> Dict:
        """Generate summary statistics about the tournament."""

        total_cards = len(self.cards)

        if total_cards == 0:
            avg_rating = 0
        else:
            total_rating = 0
            for card in self.cards.values():
                total_rating += card.rating
            avg_rating = total_rating // total_cards

        return {
            "total_cards": total_cards,
            "matches_played": self.matches_played,
            "avg_rating": avg_rating,
            "platform_status": PlatformStatus.ACTIVE.value
        }
