import pytest

from src.coordinate import Coordinate
from src.orientation import Orientation
from src.plateau import Plateau
from src.rover import Rover

plateau = Plateau(5, 5)
coordinate = Coordinate.of(0, 0)

@pytest.mark.parametrize(
    "initial, expected",
    [
        (Orientation.NORTH, Orientation.WEST),
        (Orientation.WEST, Orientation.SOUTH),
        (Orientation.SOUTH, Orientation.EAST),
        (Orientation.EAST, Orientation.NORTH),
    ]
)
def test_turn_left(initial, expected):
    rover = Rover(plateau, coordinate, initial)

    rover.turn_left()

    assert rover.orientation == expected

@pytest.mark.parametrize(
    "initial, expected",
    [
        (Orientation.NORTH, Orientation.EAST),
        (Orientation.WEST, Orientation.NORTH),
        (Orientation.SOUTH, Orientation.WEST),
        (Orientation.EAST, Orientation.SOUTH),
    ]
)
def test_turn_right(initial, expected):
    rover = Rover(plateau, coordinate, initial)

    rover.turn_right()

    assert rover.orientation == expected