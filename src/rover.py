from dataclasses import dataclass
from coordinate import Coordinate
from exceptions import ObstacleDetectedException
from orientation import Orientation
from plateau import Plateau

@dataclass
class Rover:
    plateau: Plateau
    coordinate: Coordinate
    orientation: Orientation

    def move(self):
        match self.orientation:
            case Orientation.NORTH:
                if self.coordinate.y < self.plateau.max_y:
                    self.set_new_coordinate(Coordinate.of(self.coordinate.x, self.coordinate.y + 1))
            case Orientation.SOUTH:
                if self.coordinate.y > 0:
                    self.set_new_coordinate(Coordinate.of(self.coordinate.x, self.coordinate.y - 1))
            case Orientation.EAST:
                if self.coordinate.x < self.plateau.max_x:
                    self.set_new_coordinate(Coordinate.of(self.coordinate.x + 1, self.coordinate.y))
            case Orientation.WEST:
                if self.coordinate.x > 0:
                    self.set_new_coordinate(Coordinate.of(self.coordinate.x - 1, self.coordinate.y))

    def turn_left(self):
        match self.orientation:
            case Orientation.NORTH:
                self.orientation = Orientation.WEST
            case Orientation.SOUTH:
                self.orientation = Orientation.EAST
            case Orientation.EAST:
                self.orientation = Orientation.NORTH
            case Orientation.WEST:
                self.orientation = Orientation.SOUTH

    def turn_right(self):
        match self.orientation:
            case Orientation.NORTH:
                self.orientation = Orientation.EAST
            case Orientation.EAST:
                self.orientation = Orientation.SOUTH
            case Orientation.SOUTH:
                self.orientation = Orientation.WEST
            case Orientation.WEST:
                self.orientation = Orientation.NORTH

    def set_new_coordinate(self, next_coordinate: Coordinate):
        if self.plateau.has_obstacle_at(next_coordinate):
            raise ObstacleDetectedException(f"An obstacle has been detected at the {next_coordinate}")
        self.coordinate = next_coordinate
