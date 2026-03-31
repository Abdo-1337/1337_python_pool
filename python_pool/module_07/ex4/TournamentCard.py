from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable
from typing import Dict


class TournamentCard(Card, Combatable, Rankable):
    """Card that supports combat mechanics and tournament ranking."""

    def __init__(
            self,
            name: str,
            cost: int,
            rarity: str,
            health: int,
            attack_power: int,
            defense: int,
            rating: int
            ) -> None:
        """Initialize a tournament card with combat and ranking attributes."""
        super().__init__(name, cost, rarity)
        self.health: int = health
        self.attack_power: int = attack_power
        self.defense: int = defense
        self.rating: int = rating

        self.wins: int = 0
        self.losses: int = 0

    def play(self, game_stats: Dict) -> Dict:
        """Play the card in a tournament match."""
        return {
            "card": self.name,
            "action": "played",
            "game_state": game_stats
        }

    def attack(self, target: Card) -> Dict:
        """Attack another card."""
        return {
            "attacker": self.name,
            "target": target.name,
            "damage": self.attack_power,
            "combat_resolved": True
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

    def calculate_rating(self) -> int:
        """Recalculate the rating based on wins and losses."""

        self.rating = self.rating + (self.wins * 16) - (self.losses * 16)

        return self.rating

    def update_wins(self, wins: int) -> None:
        """Increase the win count."""
        self.wins += wins

    def update_losses(self, losses: int) -> None:
        """Increase the loss count."""
        self.losses += losses

    def get_rank_info(self) -> Dict:
        """Return ranking statistics."""
        return {
            "name": self.name,
            "rating": self.rating,
            "wins": self.wins,
            "losses": self.losses
        }

    def get_combat_stats(self) -> Dict:
        """Return combat statistics."""
        return {
            "attack": self.attack_power,
            "defense": self.defense
        }

    def get_tournament_stats(self) -> Dict:
        return {
            "card": self.name,
            "rating": self.rating,
            "record": f"{self.wins}-{self.losses}"
        }
