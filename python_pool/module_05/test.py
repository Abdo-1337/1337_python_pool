from typing import Protocol


class Vehicle(Protocol):
    def move(self):
        ...


class Aircraft:
    def move(self):
        print("I fly in the sky")


class Ship:
    def move(self):
        print("I swim in the ocoan")


class Rock:
    pass


def direction(vehicle: Vehicle):
    # if hasattr(vehicle, "move"):
    #     if callable(vehicle.move):
    #         vehicle.move()
    # else:
    #     print(f"{vehicle} has not attribute move")

    # try:
    vehicle.move()
    # except AttributeError as e:
    #     print(e)
teyara = Aircraft()
safina = Ship()
hajra = Rock()
# a = 6
direction(a)