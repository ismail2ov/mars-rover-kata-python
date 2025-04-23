import pytest

from coordinate import Coordinate
from plateau import Plateau
from rover import RoverPositionedNorth, RoverPositionedEast, RoverPositionedWest, RoverPositionedSouth
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
    lambda p, p_obs: (RoverPositionedNorth(p, Coordinate.of(1, 2)), "LMLMLMLMM", RoverPositionedNorth(p, Coordinate.of(1, 3))),
    lambda p, p_obs: (RoverPositionedEast(p, Coordinate.of(3, 3)), "MMRMMRMRRM", RoverPositionedEast(p, Coordinate.of(5, 1))),
    lambda p, p_obs: (RoverPositionedNorth(p_obs, Coordinate.of(0, 0)), "MRMMRMMM", RoverPositionedEast(p_obs, Coordinate.of(0, 1))),
    lambda p, p_obs: (RoverPositionedEast(p_obs, Coordinate.of(0, 0)), "MMMLMMMLMMM", RoverPositionedWest(p_obs, Coordinate.of(3, 3)) ),
    lambda p, p_obs: (RoverPositionedNorth(p_obs, Coordinate.of(0, 0)), "MMMMMMRMMRMLMRMLMRMLMR", RoverPositionedSouth(p_obs, Coordinate.of(4, 3)))
])
def test_execute_commands(create_rovers, plateau, plateau_with_obstacles):
    initial_rover, commands, expected_rover = create_rovers(plateau, plateau_with_obstacles)
    controller = RoverController(initial_rover)

    actual = controller.run(commands)

    assert actual == expected_rover
