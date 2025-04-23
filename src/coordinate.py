from dataclasses import dataclass


@dataclass(frozen=True)
class Coordinate:
    x: int
    y: int

    @staticmethod
    def of(x: int, y: int):
        return Coordinate(x, y)