from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.GameEngine import GameEngine


def ft_data_game_engine() -> None:
    """
    Demonstrate the GameEngine using a fantasy factory
    and aggressive strategy.
    """

    print("Configuring Fantasy Card Game...")
    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()

    engine = GameEngine()
    engine.configure_engine(factory, strategy)

    print("Factory:", factory.__class__.__name__)
    print("Strategy:", strategy.get_strategy_name())
    print("Available types:", factory.get_supported_types())

    print("Simulating aggressive turn...")
    result = engine.simulate_turn()
    print()

    print("Turn execution:")
    print("Strategy:", strategy.get_strategy_name())
    print("Actions:", result)
    print()

    print("Game Report:")
    print(engine.get_engine_status())
    print()

    print("Abstract Factory + Strategy Pattern: Maximum flexibility achieved!")


def main() -> None:
    """Entry point for the DataDeck Game Engine demo."""

    print("=== DataDeck Game Engine ===")
    print()

    ft_data_game_engine()


if __name__ == "__main__":
    main()
