import pytest

from coordinate import Coordinate
from plateau import Plateau
from rover import RoverPositionedNorth, RoverPositionedWest, RoverPositionedSouth, RoverPositionedEast

MIN_X = 0
MIN_Y = 0
MID_X = 3
MID_Y = 3
MAX_X = 5
MAX_Y = 5


@pytest.fixture(scope="module")
def plateau():
    return Plateau(MAX_X, MAX_Y)


@pytest.mark.parametrize("rover, expected_coordinate", [
    (lambda p: RoverPositionedNorth(p, Coordinate.of(MIN_X, MIN_Y)), Coordinate.of(MIN_X, MIN_Y + 1)),
    (lambda p: RoverPositionedNorth(p, Coordinate.of(MID_X, MID_Y)), Coordinate.of(MID_X, MID_Y + 1)),
    (lambda p: RoverPositionedNorth(p, Coordinate.of(MAX_X, MAX_Y)), Coordinate.of(MAX_X, MAX_Y)),

    (lambda p: RoverPositionedWest(p, Coordinate.of(MIN_X, MIN_Y)), Coordinate.of(MIN_X, MIN_Y)),
    (lambda p: RoverPositionedWest(p, Coordinate.of(MID_X, MID_Y)), Coordinate.of(MID_X - 1, MID_Y)),
    (lambda p: RoverPositionedWest(p, Coordinate.of(MAX_X, MAX_Y)), Coordinate.of(4, MAX_Y)),

    (lambda p: RoverPositionedSouth(p, Coordinate.of(MIN_X, MIN_Y)), Coordinate.of(MIN_X, MIN_Y)),
    (lambda p: RoverPositionedSouth(p, Coordinate.of(MID_X, MID_Y)), Coordinate.of(MID_X, MID_Y - 1)),
    (lambda p: RoverPositionedSouth(p, Coordinate.of(MAX_X, MAX_Y)), Coordinate.of(MAX_X, MAX_Y - 1)),

    (lambda p: RoverPositionedEast(p, Coordinate.of(MIN_X, MIN_Y)), Coordinate.of(MIN_X + 1, MIN_Y)),
    (lambda p: RoverPositionedEast(p, Coordinate.of(MID_X, MID_Y)), Coordinate.of(MID_X + 1, MID_Y)),
    (lambda p: RoverPositionedEast(p, Coordinate.of(MAX_X, MAX_Y)), Coordinate.of(MAX_X, MAX_Y))
])
def test_rover_should_move_to(plateau, rover, expected_coordinate):
    actual = rover(plateau).move()

    assert actual.coordinate == expected_coordinate
