from typing import Dict, List
from ex0.Card import Card
from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine:
    """Core engine that coordinates card creation and strategy execution."""

    def configure_engine(
            self,
            factory: CardFactory,
            strategy: GameStrategy
                ) -> None:
        """Configure the game engine with a card factory and strategy."""
        self.factory: CardFactory = factory
        self.strategy: GameStrategy = strategy

        self.turns_simulated = 0
        self.total_damage = 0
        self.cards_created = 0

    def simulate_turn(self) -> Dict:
        """Simulate a single turn using the configured strategy."""
        battlefield: List[Card] = []

        hand = [
            self.factory.create_creature("Fire Dragon"),
            self.factory.create_creature("Goblin Warrior"),
            self.factory.create_spell("Lightning Bolt")
        ]

        print("Hand: [", end="")

        for i, card in enumerate(hand):
            if i == len(hand) - 1:
                print(f"{card.name} ({card.cost})", end="")
            else:
                print(f"{card.name} ({card.cost})", end=", ")

        print("]")

        battlefield = [
            card for card in hand if hasattr(card, "attack")
            ]

        result = self.strategy.execute_turn(hand, battlefield)
        self.turns_simulated += 1
        self.total_damage += result["damage_dealt"]
        self.cards_created += len(hand)

        return result

    def get_engine_status(self) -> Dict:
        """Return the current statistics of the game engine."""
        return {
            "turns_simulated": self.turns_simulated,
            "strategy_used": self.strategy.get_strategy_name(),
            "total_damage": self.total_damage,
            "cards_created": self.cards_created
        }
