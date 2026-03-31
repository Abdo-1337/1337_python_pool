from abc import ABC, abstractmethod
from typing import Dict, List
from ex0.Card import Card
from enum import Enum


class StrategyName(Enum):
    """Enumeration of available strategy names."""

    AGGRESSIVE = "AggressiveStrategy"
    DEFENSIVE = "DefensiveStrategy"


class GameStrategy(ABC):
    """Abstract interface for defining game strategies."""

    @abstractmethod
    def execute_turn(
        self,
        hand: List[Card],
        battlefield: List[Card]
            ) -> Dict:
        """Execute a turn based on the current hand and battlefield."""
        pass

    @abstractmethod
    def get_strategy_name(self) -> str:
        """Return the name of the strategy."""
        pass

    @abstractmethod
    def prioritize_targets(
        self,
        available_targets: List[Card]
            ) -> List[str]:
        """Prioritize targets according to the strategy."""
        pass
