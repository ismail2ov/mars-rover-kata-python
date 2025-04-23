from dataclasses import dataclass, replace

from coordinate import Coordinate
from exceptions import ObstacleDetectedException
from orientation import Orientation
from plateau import Plateau


@dataclass(frozen=True)
class Rover:
    plateau: Plateau
    coordinate: Coordinate
    orientation: Orientation

    def move(self):
        new_coordinate = self.coordinate

        match self.orientation:
            case Orientation.NORTH:
                if self.coordinate.y < self.plateau.max_y:
                    new_coordinate = self._get_valid_coordinate(
                        Coordinate.of(self.coordinate.x, self.coordinate.y + 1)
                    )
            case Orientation.SOUTH:
                if self.coordinate.y > 0:
                    new_coordinate = self._get_valid_coordinate(
                        Coordinate.of(self.coordinate.x, self.coordinate.y - 1)
                    )
            case Orientation.EAST:
                if self.coordinate.x < self.plateau.max_x:
                    new_coordinate = self._get_valid_coordinate(
                        Coordinate.of(self.coordinate.x + 1, self.coordinate.y)
                    )
            case Orientation.WEST:
                if self.coordinate.x > 0:
                    new_coordinate = self._get_valid_coordinate(
                        Coordinate.of(self.coordinate.x - 1, self.coordinate.y)
                    )

        return replace(self, coordinate=new_coordinate)

    def turn_left(self) -> "Rover":
        new_orientation = {
            Orientation.NORTH: Orientation.WEST,
            Orientation.WEST: Orientation.SOUTH,
            Orientation.SOUTH: Orientation.EAST,
            Orientation.EAST: Orientation.NORTH
        }[self.orientation]

        return replace(self, orientation=new_orientation)

    def turn_right(self) -> "Rover":
        new_orientation = {
            Orientation.NORTH: Orientation.EAST,
            Orientation.EAST: Orientation.SOUTH,
            Orientation.SOUTH: Orientation.WEST,
            Orientation.WEST: Orientation.NORTH
        }[self.orientation]

        return replace(self, orientation=new_orientation)

    def _get_valid_coordinate(self, next_coordinate: Coordinate) -> Coordinate:
        if self.plateau.has_obstacle_at(next_coordinate):
            raise ObstacleDetectedException(f"An obstacle has been detected at {next_coordinate}")
        return next_coordinate