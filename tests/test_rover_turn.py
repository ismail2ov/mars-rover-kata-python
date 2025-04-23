import pytest

from coordinate import Coordinate
from orientation import Orientation
from plateau import Plateau
from rover import RoverPositionedNorth, RoverPositionedWest, RoverPositionedSouth, RoverPositionedEast

plateau = Plateau(5, 5)
coordinate = Coordinate.of(0, 0)

@pytest.mark.parametrize("rover, expected_orientation", [
    (RoverPositionedNorth(plateau, coordinate), Orientation.WEST),
    (RoverPositionedWest(plateau, coordinate), Orientation.SOUTH),
    (RoverPositionedSouth(plateau, coordinate), Orientation.EAST),
    (RoverPositionedEast(plateau, coordinate), Orientation.NORTH),
])
def test_turn_left(rover, expected_orientation):
    actual = rover.turn_left()

    assert actual.orientation == expected_orientation

@pytest.mark.parametrize("rover, expected_orientation", [
    (RoverPositionedNorth(plateau, coordinate), Orientation.EAST),
    (RoverPositionedWest(plateau, coordinate), Orientation.NORTH),
    (RoverPositionedSouth(plateau, coordinate), Orientation.WEST),
    (RoverPositionedEast(plateau, coordinate), Orientation.SOUTH),
])
def test_turn_right(rover, expected_orientation):
    actual = rover.turn_right()

    assert actual.orientation == expected_orientation