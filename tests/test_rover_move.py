import pytest

from coordinate import Coordinate
from orientation import Orientation
from plateau import Plateau
from rover import Rover

MIN_X = 0
MIN_Y = 0
MID_X = 3
MID_Y = 3
MAX_X = 5
MAX_Y = 5

plateau = Plateau(MAX_X, MAX_Y)


@pytest.mark.parametrize(
    "initial, orientation, expected",
    [
        (Coordinate.of(MIN_X, MIN_Y), Orientation.NORTH, Coordinate.of(MIN_X, MIN_Y + 1)),
        (Coordinate.of(MID_X, MID_Y), Orientation.NORTH, Coordinate.of(MID_X, MID_Y + 1)),
        (Coordinate.of(MAX_X, MAX_Y), Orientation.NORTH, Coordinate.of(MAX_X, MAX_Y)),

        (Coordinate.of(MIN_X, MIN_Y), Orientation.WEST, Coordinate.of(MIN_X, MIN_Y)),
        (Coordinate.of(MID_X, MID_Y), Orientation.WEST, Coordinate.of(MID_X - 1, MID_Y)),
        (Coordinate.of(MAX_X, MAX_Y), Orientation.WEST, Coordinate.of(4, MAX_Y)),

        (Coordinate.of(MIN_X, MIN_Y), Orientation.SOUTH, Coordinate.of(MIN_X, MIN_Y)),
        (Coordinate.of(MID_X, MID_Y), Orientation.SOUTH, Coordinate.of(MID_X, MID_Y - 1)),
        (Coordinate.of(MAX_X, MAX_Y), Orientation.SOUTH, Coordinate.of(MAX_X, MAX_Y - 1)),

        (Coordinate.of(MIN_X, MIN_Y), Orientation.EAST, Coordinate.of(MIN_X + 1, MIN_Y)),
        (Coordinate.of(MID_X, MID_Y), Orientation.EAST, Coordinate.of(MID_X + 1, MID_Y)),
        (Coordinate.of(MAX_X, MAX_Y), Orientation.EAST, Coordinate.of(MAX_X, MAX_Y)),
    ]
)
def test_rover_should_move_to(initial, orientation, expected):
    rover = Rover(plateau, initial, orientation)
    rover.move()
    assert rover.coordinate == expected
