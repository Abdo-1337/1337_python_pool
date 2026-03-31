from abc import ABC, abstractmethod
from typing import Dict, List


class Magical(ABC):
    """Interface defining magical abilities for cards."""

    @abstractmethod
    def cast_spell(self, spell_name: str, targets: List[str]) -> Dict:
        """Cast a spell on one or more targets."""
        pass

    @abstractmethod
    def channel_mana(self, amount: int) -> Dict:
        """Increase the available mana."""
        pass

    @abstractmethod
    def get_magic_stats(self) -> Dict[str, object]:
        """Return magic-related statistics."""
        pass
