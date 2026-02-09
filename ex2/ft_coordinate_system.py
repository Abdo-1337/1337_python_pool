import sys
import math


def ft_coordinate_system():
    """
    Demonstrates tuple usage through a simple 3D coordinate system.

    - Creates fixed 3D positions using tuples.
    - Unpacks tuple values into individual coordinates.
    - Calculates Euclidean distance between two 3D points.
    - Parses coordinates from command-line input formatted as "x,y,z".
    - Handles invalid input using exception handling.
    - Demonstrates tuple immutability and unpacking for readability.
    """
    print("=== Game Coordinate System ===\n")

    pos_1 = (0, 0, 0)
    pos_2 = (10, 20, 5)
    x1, y1, z1 = pos_1
    x2, y2, z2 = pos_2
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
    print(f"Position created: {pos_1}")
    print(f"Distance between {pos_1} and {pos_2}: %.2f\n" % distance)

    try:
        count = len(sys.argv)
        if count == 1:
            raise ValueError("invalid literal for int() with base 10: \'\'")
    except ValueError as e:
        raise e
    try:
        count = len(sys.argv)
        if count == 1:
            raise ValueError("Error")
        positions_list = (sys.argv[1].split(','))
        if len(positions_list) < 3:
            raise ValueError(
                "Error parsing coordinates: expected 3 values (x,y,z)"
                )
        posistion_coordinates = []
        i = 0
        while i < 3:
            posistion_coordinates += [int(positions_list[i])]
            i += 1
        position_tuple = tuple()
        position_tuple = tuple(posistion_coordinates)
        print("Parsing coordinates: \"", end="")
        i = 0
        while i < 3:
            print(position_tuple[i], end="")
            if i < 2:
                print(',', end="")
            else:
                print("\"")
            i += 1
        print("Parsed postion:", position_tuple)
        x2, y2, z2 = position_tuple
        distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
        print(f"Distance between {pos_1} and {position_tuple}: "
              f"%.1f\n" % distance)
        print("Unpacking demonstration")
        print(f"Player at x={x2}, y={y2}, z={z2}")
        print(f"Coordinates: X={x2}, Y={y2}, Z={z2}")
    except ValueError as e:
        print(f"Parsing invalid coordinates: \"{sys.argv[1]}\"")
        raise e


if __name__ == "__main__":
    try:
        ft_coordinate_system()
    except ValueError as e:
        print("Error parsing coordinates:", e)
        print(f"Error details - Type: ValueError, Args: (\"{e}\")")
