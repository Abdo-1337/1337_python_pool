from alchemy.transmutation.basic import lead_to_gold, stone_to_gem
from alchemy.transmutation.advanced import philosophers_stone, elexir_of_life
from alchemy.transmutation import lead_to_gold, philosophers_stone


def ft_absolute_imports() -> None:
    print("Testing Absolute Imports (from basic.py):")
    print("lead_to_gold():", lead_to_gold())
    print("stone_to_gem():", stone_to_gem())


def ft_relative_imports() -> None:
    print("Testing Relative Imports (from advanced.py):")
    print("philosophers_stone():", philosophers_stone())
    print("elixir_of_life():", elexir_of_life())


def ft_package_imports() -> None:
    print("Testing Package Access:")
    print("alchemy.transmutation.lead_to_gold():", lead_to_gold())
    print("alchemy.transmutation.philosophers_stone():", philosophers_stone())


def main() -> None:
    print()
    print("=== Pathway Debate Mastery ===")
    print()

    ft_absolute_imports()
    print()

    ft_relative_imports()
    print()

    ft_package_imports()
    print()

    print("Both pathways work! Absolute: clear, Relative: concise")


if __name__ == "__main__":
    main()