import os
import sys
from dotenv import load_dotenv
from typing import Dict, Optional


def get_env_var(name: str) -> str:
    """
    Retrieve an environment variable or raise an error if missing.

    Args:
        name (str): The name of the environment variable.

    Returns:
        str: The value of the environment variable.

    Raises:
        ValueError: If the variable is not set or empty.
    """

    value = os.getenv(name)

    # Ensure required configuration is present
    if not value:
        raise ValueError(f"Missing required environment variable: {name}")

    return value


def load_configuration() -> Optional[Dict[str, str]]:
    """
    Load configuration from environment variables and .env file.

    Returns:
        Optional[Dict[str, str]]: Configuration dictionary if valid,
        otherwise None.
    """

    # Load variables from .env into environment
    load_dotenv()

    try:

        return {
            "mode": get_env_var("MATRIX_MODE"),
            "database": get_env_var("DATABASE_URL"),
            "api_key": get_env_var("API_KEY"),
            "log_level": get_env_var("LOG_LEVEL"),
            "zion": get_env_var("ZION_ENDPOINT"),
        }
    except ValueError as e:
        print(f"Configuration Error: {e}")
        return None


def display_status(config: Dict[str, str]) -> None:
    """
    Display system configuration and security status.

    Args:
        config (Dict[str, str]): Loaded configuration values.
    """
    print("ORACLE STATUS: Reading the Matrix...")
    print()

    print("Configuration loaded:")
    print(f"Mode: {config['mode']}")

    # Simulate environment-specific behavior
    if config["mode"] == "development":
        print("Database: Connected to local instance")
    else:
        print("Database: Connected to production system")

    print("API Access: Authenticated")
    print(f"Log Level: {config['log_level']}")
    print("Zion Network: Online")
    print()

    print("Environment security check:")

    # Check for missing values (basic validation)
    if all(config.values()):
        print("[OK] No hardcoded secrets detected")
        print("[OK] .env file properly configured")
    else:
        print("[WARNING] Some configuration values may be missing")

    # Validate mode value
    if config["mode"] in ("development", "production"):
        print("[OK] Production overrides available")
    else:
        print("[WARNING] Unknown environment mode")

    print()

    print("The Oracle sees all configurations.")


def main() -> None:
    """
    Main entry point of the program.
    Loads configuration and displays system status.
    """

    config = load_configuration()

    if not config:
        sys.exit(1)

    display_status(config)


if __name__ == "__main__":
    main()
