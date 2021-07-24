from __future__ import annotations
from math import sqrt

class Vector:
    """
    Vector object.

    Can be added and subtracted, and multiplied 
    to the left by a scalar as expected.
    Attributes:
        x, y
    Method:
        norm
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def norm(self) -> float:
        return sqrt(self.x ** 2 + self.y ** 2)

    def __rmul__(self, other: float) -> Vector:
        return Vector(other * self.x, other * self.y)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __str__(self):
        return f'x: {self.x}, y: {self.y}'


def distance(position_1: Vector, position_2: Vector) -> float:
    """Compute the distance between two positions using the Vector class."""
    vector = position_1 - position_2
    return vector.norm()
