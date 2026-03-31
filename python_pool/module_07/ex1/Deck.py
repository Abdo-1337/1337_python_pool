from ex0.Card import Card
from typing import Dict, List
import random


class Deck:
    """Represents a collection of cards that can be managed and played."""
    def __init__(self):
        """Initialize an empty deck."""
        self.cards: List[Card] = []

    def add_card(self, card: Card) -> None:
        """Add a card to the deck."""
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        """Remove a card from the deck by name."""
        for card in self.cards:
            if card.name == card_name:
                self.cards.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        """Shuffle the deck randomly."""
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        """Draw the top card from the deck."""
        if not self.cards:
            raise ValueError("Cannot draw from an empty deck")
        return self.cards.pop(0)

    def get_deck_stats(self) -> Dict:
        """Return statistics about the deck composition."""
        total_cards = len(self.cards)

        creature_cards = 0
        spells_cards = 0
        artifacts_cards = 0

        for card in self.cards:
            card_type = card.get_card_info()["type"]

            if card_type == "Creature":
                creature_cards += 1

            elif card_type == "Spell":
                spells_cards += 1

            elif card_type == "Artifact":
                artifacts_cards += 1

        total_cost = 0
        for card in self.cards:

            total_cost += card.cost

        if not total_cards:
            avg_cost = 0.0
        else:
            avg_cost = total_cost / total_cards

        return {
            "total_cards": total_cards,
            "creatures": creature_cards,
            "spells": spells_cards,
            "artifacts": artifacts_cards,
            "avg_cost": avg_cost
        }
