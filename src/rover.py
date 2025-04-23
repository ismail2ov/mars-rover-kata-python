from abc import ABC, abstractmethod

from coordinate import Coordinate
from exceptions import ObstacleDetectedException
from orientation import Orientation
from plateau import Plateau


class Rover(ABC):
    def __init__(self, plateau: Plateau, coordinate: Coordinate, orientation: Orientation):
        if plateau.has_obstacle_at(coordinate):
            raise ObstacleDetectedException(f"An obstacle has been detected at the {coordinate}")
        self._plateau = plateau
        self._coordinate = coordinate
        self._orientation = orientation

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def turn_left(self):
        pass

    @abstractmethod
    def turn_right(self):
        pass

    @property
    def plateau(self):
        return self._plateau

    @property
    def coordinate(self):
        return self._coordinate

    @property
    def orientation(self):
        return self._orientation

    def __eq__(self, other):
        return (
                isinstance(other, Rover)
                and self._plateau == other._plateau
                and self._coordinate == other._coordinate
                and self._orientation == other._orientation
        )


class RoverPositionedEast(Rover):
    ORIENTATION = Orientation.EAST

    def __init__(self, plateau, coordinate):
        super().__init__(plateau, coordinate, self.ORIENTATION)

    def move(self):
        if self.coordinate.x < self.plateau.max_x:
            return RoverPositionedEast(self.plateau, Coordinate.of(self.coordinate.x + 1, self.coordinate.y))
        return self

    def turn_left(self):
        return RoverPositionedNorth(self.plateau, self.coordinate)

    def turn_right(self):
        return RoverPositionedSouth(self.plateau, self.coordinate)


class RoverPositionedNorth(Rover):
    ORIENTATION = Orientation.NORTH

    def __init__(self, plateau, coordinate):
        super().__init__(plateau, coordinate, self.ORIENTATION)

    def move(self):
        if self.coordinate.y < self.plateau.max_y:
            return RoverPositionedNorth(self.plateau, Coordinate.of(self.coordinate.x, self.coordinate.y + 1))
        return self

    def turn_left(self):
        return RoverPositionedWest(self.plateau, self.coordinate)

    def turn_right(self):
        return RoverPositionedEast(self.plateau, self.coordinate)


class RoverPositionedSouth(Rover):
    ORIENTATION = Orientation.SOUTH

    def __init__(self, plateau, coordinate):
        super().__init__(plateau, coordinate, self.ORIENTATION)

    def move(self):
        if self.coordinate.y > 0:
            return RoverPositionedSouth(self.plateau, Coordinate.of(self.coordinate.x, self.coordinate.y - 1))
        return self

    def turn_left(self):
        return RoverPositionedEast(self.plateau, self.coordinate)

    def turn_right(self):
        return RoverPositionedWest(self.plateau, self.coordinate)


class RoverPositionedWest(Rover):
    ORIENTATION = Orientation.WEST

    def __init__(self, plateau, coordinate):
        super().__init__(plateau, coordinate, self.ORIENTATION)

    def move(self):
        if self.coordinate.x > 0:
            return RoverPositionedWest(self.plateau, Coordinate.of(self.coordinate.x - 1, self.coordinate.y))
        return self

    def turn_left(self):
        return RoverPositionedSouth(self.plateau, self.coordinate)

    def turn_right(self):
        return RoverPositionedNorth(self.plateau, self.coordinate)
