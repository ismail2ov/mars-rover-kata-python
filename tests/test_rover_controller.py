import pytest

from orientation import Orientation
from coordinate import Coordinate
from plateau import Plateau
from rover import Rover
from rover_controller import RoverController


@pytest.fixture(scope="module")
def plateau():
    return Plateau(5, 5)

@pytest.fixture(scope="module")
def plateau_with_obstacles():
    plateau = Plateau(5, 5)
    plateau.add_obstacle(Coordinate.of(1, 1))
    plateau.add_obstacle(Coordinate.of(2, 3))
    plateau.add_obstacle(Coordinate.of(4, 2))
    return plateau

@pytest.mark.parametrize("create_rovers", [
    lambda p, p_obs: (Rover(p, Coordinate.of(1, 2), Orientation.NORTH), "LMLMLMLMM", Rover(p, Coordinate.of(1, 3), Orientation.NORTH)),
    lambda p, p_obs: (Rover(p, Coordinate.of(3, 3), Orientation.EAST), "MMRMMRMRRM", Rover(p, Coordinate.of(5, 1), Orientation.EAST)),
    lambda p, p_obs: (Rover(p_obs, Coordinate.of(0, 0), Orientation.NORTH), "MRMMRMMM", Rover(p_obs, Coordinate.of(0, 1), Orientation.EAST)),
    lambda p, p_obs: (Rover(p_obs, Coordinate.of(0, 0), Orientation.EAST), "MMMLMMMLMMM", Rover(p_obs, Coordinate.of(3, 3), Orientation.WEST)),
    lambda p, p_obs: (Rover(p_obs, Coordinate.of(0, 0), Orientation.NORTH), "MMMMMMRMMRMLMRMLMRMLMR", Rover(p_obs, Coordinate.of(4, 3), Orientation.SOUTH))
])
def test_execute_commands(create_rovers, plateau, plateau_with_obstacles):
    initial, commands, expected = create_rovers(plateau, plateau_with_obstacles)
    rover_controller = RoverController(initial)
    rover_controller.run(commands)

    assert initial.coordinate == expected.coordinate
    assert initial.orientation == expected.orientation
