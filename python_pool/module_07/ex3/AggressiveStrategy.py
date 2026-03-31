from typing import List, Dict
from ex3.GameStrategy import GameStrategy, StrategyName
from ex0.Card import Card


class AggressiveStrategy(GameStrategy):
    """Strategy that prioritizes attacking and dealing maximum damage."""

    def execute_turn(
            self,
            hand: List[Card],
            battlefield: List[Card]
                ) -> Dict:
        """Execute a turn focusing on aggressive play."""
        MAX_MANA = 5
        cards_to_play: List[Card] = []
        mana_used = 0
        damage_dealt = 0
        targets_attacked: List[Card] = []

        self.prioritize_targets(hand)
        for card in reversed(hand):
            if mana_used + card.cost <= MAX_MANA:
                cards_to_play.append(card.name)
                mana_used += card.cost
                damage_dealt += 4
            else:
                break

        for card in battlefield:
            if hasattr(card, "attack_power"):
                damage_dealt += card.attack_power

        targets_attacked.append("Enemy Player")

        return {
            "cards_played": cards_to_play,
            "mana_used": mana_used,
            "targets_attacked": targets_attacked,
            "damage_dealt": damage_dealt
        }

    def get_strategy_name(self) -> str:
        """Return the strategy name."""
        return StrategyName.AGGRESSIVE.value

    def prioritize_targets(
            self,
            available_targets: List[Card]
                ) -> List[Card]:
        """Sort targets by descending cost."""
        swapped = True
        while swapped:
            swapped = False
            for x in range(len(available_targets) - 1):
                if available_targets[x].cost < available_targets[x + 1].cost:
                    available_targets[x], available_targets[x + 1] = (
                        available_targets[x + 1], available_targets[x]
                    )
                    swapped = True
        return available_targets
