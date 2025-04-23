from dataclasses import dataclass

from src.coordinate import Coordinate
from src.orientation import Orientation
from src.plateau import Plateau


@dataclass
class Rover:
    plateau: Plateau
    coordinate: Coordinate
    orientation: Orientation.NORTH

    def move(self):
        self.coordinate = Coordinate(self.coordinate.x, self.coordinate.y + 1)