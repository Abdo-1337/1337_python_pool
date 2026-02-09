import sys


def main():
    """
    Reads and displays command-line arguments using sys.argv.
    """
    count = len(sys.argv)
    print("=== Command Quest ===")
    if count == 1:
        print("No arguments provided!")
        print("Program name:", sys.argv[0])
        print(f"Total arguments: {count}\n")
    else:
        print("Program name:", sys.argv[0])
        print(f"Arguments received: {count - 1}")
        i = 1
        while i < count:
            print(f"Argument {i}: {sys.argv[i]}")
            i += 1
        print(f"Total arguments: {count}\n")


if __name__ == "__main__":
    main()
