import alchemy.elements
from alchemy.elements import create_water
from alchemy.potions import healing_potion as heal, strength_potion
from alchemy.elements import create_fire, create_earth


def ft_full_module_import() -> None:
    print("Method 1 - Full module import:")
    print("alchemy.elements.create_fire():", alchemy.elements.create_fire())


def ft_specific_import() -> None:
    print("Method 2 - Specific function import:")
    print("create_water():", create_water())


def ft_aliased_import() -> None:
    print("Method 3 - Aliased import:")
    print("heal:", heal())


def ft_multiple_imports() -> None:
    print("Method 4 - Multiple imports:")
    print("create_earth():", create_earth())
    print("create_file():", create_fire())
    print("strength_potion():", strength_potion())


def main() -> None:
    print("=== Import Transmutation Mastery ===")

    print()
    ft_full_module_import()

    print()
    ft_specific_import()

    print()
    ft_aliased_import()

    print()
    ft_multiple_imports()

    print()
    print("All import transmutation methods mastered!")


if __name__ == "__main__":
    main()
