from typing import List

from coordinate import Coordinate


class Plateau:
    def __init__(self, max_x: int, max_y: int):
        self.max_x = max_x
        self.max_y = max_y
        self.obstacles: List[Coordinate] = []

    def add_obstacle(self, obstacle: Coordinate):
        self.obstacles.append(obstacle)

    def has_obstacle_at(self, next_coordinate: Coordinate) -> bool:
        return next_coordinate in self.obstacles
