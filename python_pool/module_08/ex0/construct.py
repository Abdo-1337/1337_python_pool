import sys
import os
import site


def is_in_venv() -> bool:
    """
    Check if the script is running inside a virtual environment.

    Returns:
        bool: True if inside a virtual environment, False otherwise.
    """

    # In a virtual environment, sys.prefix differs from sys.base_prefix
    return sys.prefix != sys.base_prefix


def show_inside_venv() -> None:
    """
    Display information about the active virtual environment.
    """
    # Extract environment name from its path
    env_name = os.path.basename(sys.prefix)

    # Full path to the virtual environment
    env_path = sys.prefix

    # Get installation paths for packages
    site_packages = site.getsitepackages()

    print("MATRIX STATUS: Welcome to the construct")
    print()
    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment: {env_name}")
    print()
    print(f"Environment Path: {env_path}")
    print()
    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting the global system.")
    print()
    print(f"Package installation path: {site_packages[0]}")


def show_outside_venv() -> None:
    """
    Display warning and instructions when not in a virtual environment.
    """

    print("MATRIX STATUS: You're still plugged in")
    print()
    print(f"Current Python: {sys.executable}")
    print("Virtual Environment: None detected")
    print()
    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.")
    print()
    print("To enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate # On Unix")
    print("matrix_env")
    print("Scripts")
    print("activate # On Windows")
    print()
    print("Then run this program again.")


def main() -> None:
    """
    Main entry point of the program.
    Determines environment and displays appropriate information.
    """

    if is_in_venv():
        show_inside_venv()
    else:
        show_outside_venv()


if __name__ == "__main__":
    main()
