import alchemy


def ft_direct_module_access() -> None:
    print("Testing direct module access:")

    print("alchemy.elements.create_fire():", alchemy.elements.create_fire())
    print("alchemy.elements.create_water():", alchemy.elements.create_water())
    print("alchemy.elements.create_earth():", alchemy.elements.create_earth())
    print("alchemy.elements.create_air():", alchemy.elements.create_air())


def ft_package_level_access() -> None:
    print("Testing package-level access (controlled by __init__.py):")
    try:
        print("alchemy.create_fire():", alchemy.create_fire())
    except AttributeError:
        print("alchemy.create_fire(): AttributeError - not exposed")

    try:
        print("alchemy.create_water():", alchemy.create_water())
    except AttributeError:
        print("alchemy.create_water(): AttributeError - not exposed")

    try:
        print("alchemy.create_earth():", alchemy.create_earth())
    except AttributeError:
        print("alchemy.create_earth(): AttributeError - not exposed")

    try:
        print("alchemy.create_air():", alchemy.create_air())
    except AttributeError:
        print("alchemy.create_air(): AttributeError - not exposed")


def ft_package_metadata() -> None:
    print("Package metadata:")

    print("Version:", alchemy.__version__)
    print("Author:", alchemy.__author__)


def main() -> None:
    print("=== Sacred Scroll Mastery ===")
    print()

    ft_direct_module_access()

    print()

    ft_package_level_access()

    print()

    ft_package_metadata()


if __name__ == "__main__":
    main()
