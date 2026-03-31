from abc import ABC, abstractmethod
from typing import Dict


class Rankable(ABC):
    """Abstract interface for objects that can be ranked in a tournament."""

    @abstractmethod
    def calculate_rating(self) -> int:
        """Calculate and return the current rating of the object."""
        pass

    @abstractmethod
    def update_wins(self, wins: int) -> None:
        """Update the number of wins."""
        pass

    @abstractmethod
    def update_losses(self, losses: int) -> None:
        """Update the number of losses."""
        pass

    @abstractmethod
    def get_rank_info(self) -> Dict:
        """Return ranking information as a dictionary."""
        pass
