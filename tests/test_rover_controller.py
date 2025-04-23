import pytest

from src.coordinate import Coordinate
from src.orientation import Orientation
from src.plateau import Plateau
from src.rover import Rover
from src.rover_controller import RoverController


@pytest.mark.parametrize(
    "initial, commands, expected",
    [
        (Rover(Plateau(5, 5), Coordinate(1, 2), Orientation.NORTH), "LMLMLMLMM", Rover(Plateau(5, 5), Coordinate(1, 3), Orientation.NORTH)),
        (Rover(Plateau(5, 5), Coordinate(3, 3), Orientation.EAST), "MMRMMRMRRM", Rover(Plateau(5, 5), Coordinate(5, 1), Orientation.EAST))
    ]
)
def test_execute_commands(initial, commands, expected):
    rover_controller = RoverController(initial)
    rover_controller.run(commands)

    assert initial.coordinate == expected.coordinate
    assert initial.orientation == expected.orientation
