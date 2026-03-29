import importlib
from typing import Dict, Optional
import sys


def get_dependency(name: str) -> Optional[object]:
    """
    Try to import a dependency dynamically.

    Args:
        name (str): Name of the module to import.

    Returns:
        Optional[object]: The imported module if available, otherwise None.
    """
    try:

        # Dynamically import module to avoid crashing if missing
        module = importlib.import_module(name)

        # Safely retrieve version (not all modules define __version__)
        version = getattr(module, "__version__", "unknown")
        print(f"[OK] {name} ({version}) - ready")

        return module

    except ImportError:
        print(f"[MISSING] {name} - not installed")
        return None


def check_dependencies() -> Dict[str, Optional[object]]:
    """
    Check availability of required dependencies.

    Returns:
        Dict[str, Optional[object]]: Mapping of dependency names to modules.
    """

    print("Checking dependencies:")

    deps = {
        "pandas": get_dependency("pandas"),
        "numpy": get_dependency("numpy"),
        "matplotlib": get_dependency("matplotlib")
    }

    return deps


def run_analysis() -> None:
    """
    Perform data analysis and generate a visualization.
    Only executed if all dependencies are available.
    """
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt

    print()
    print("Analyzing Matrix data...")
    print("Processing 1000 data points...")

    # Generate random dataset
    data = np.random.randn(1000)

    # Convert to DataFrame (tabular structure)
    df = pd.DataFrame(data, columns=["values"])

    print("Generating visualization...")

    # Save plot instead of displaying (non-interactive execution)
    plt.hist(df["values"], bins=30)
    plt.savefig("matrix_analysis.png")
    plt.close()

    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


def show_install_instructions() -> None:
    """
    Display instructions to install missing dependencies.
    """
    print()
    print("Some dependencies are missing.")
    print("Install them using:")
    print("pip install -r requirements.txt")
    print("or")
    print("poetry install")


def main() -> None:
    """
    Main entry point of the program.
    Checks dependencies and runs analysis if possible.
    """
    print("LOADING STATUS: Loading programs...")
    print()

    deps = check_dependencies()

    # Ensure all dependencies are available before proceeding
    if not all(deps.values()):
        show_install_instructions()
        sys.exit(1)

    run_analysis()


if __name__ == "__main__":
    main()
