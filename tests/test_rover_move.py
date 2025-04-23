import pytest

from src.coordinate import Coordinate
from src.orientation import Orientation
from src.plateau import Plateau
from src.rover import Rover


def test_should_move_north():
    plateau = Plateau(5, 5)
    coordinate = Coordinate(0, 0)
    orientation = Orientation.NORTH
    rover = Rover(plateau, coordinate, orientation)
    expected = Coordinate(0, 1)

    rover.move()

    assert rover.coordinate == expected