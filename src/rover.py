from dataclasses import dataclass

from src.coordinate import Coordinate
from src.orientation import Orientation
from src.plateau import Plateau


@dataclass
class Rover:
    plateau: Plateau
    coordinate: Coordinate
    orientation: Orientation

    def move(self):
        x, y = self.coordinate.x, self.coordinate.y

        match self.orientation:
            case Orientation.NORTH:
                if y < self.plateau.max_y:
                    self.coordinate = Coordinate.of(x, y + 1)
            case Orientation.SOUTH:
                if y > 0:
                    self.coordinate = Coordinate.of(x, y - 1)
            case Orientation.EAST:
                if x < self.plateau.max_x:
                    self.coordinate = Coordinate.of(x + 1, y)
            case Orientation.WEST:
                if x > 0:
                    self.coordinate = Coordinate.of(x - 1, y)

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
