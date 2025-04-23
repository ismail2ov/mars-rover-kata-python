import pytest

from src.coordinate import Coordinate
from src.orientation import Orientation
from src.plateau import Plateau
from src.rover import Rover


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
    plateau = Plateau(5, 5)
    coordinate = Coordinate.of(0, 0)
    rover = Rover(plateau, coordinate, initial)

    rover.turn_left()

    assert rover.orientation == expected
