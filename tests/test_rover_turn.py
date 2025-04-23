import pytest

from coordinate import Coordinate
from orientation import Orientation
from plateau import Plateau
from rover import Rover

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

    actual = rover.turn_left()

    assert actual.orientation == expected

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

    actual = rover.turn_right()

    assert actual.orientation == expected