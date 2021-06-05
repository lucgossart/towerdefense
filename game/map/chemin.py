from abc         import ABC, abstractmethod
from math        import sqrt

from game.vector import Vector

class Path:
    @abstractmethod
    def path(x, y):
        pass

class NewPath(Path):
    def __init__(self, city_width, map_width, map_height):
        self.city_width = city_width
        self.map_width  = map_width
        self.map_height = map_height
    def path(self, x, y):
        if x <= self.city_width or x >= self.map_width - self.city_width:
            return Vector(0, 1)
        if y <= self.city_width or y >= self.map_height - self.city_width:
            return Vector(-1, 0)
        return Vector(-1 / sqrt(2), -1 / sqrt(2))


class DefaultPath(Path):
    @staticmethod
    def path(x, y):
        if 80 <= x <= 520:
            if 100 <= y <= 200 or 500 <= y <= 600:
                return Vector(-1, 0)
        if 40 <= x <= 500:
            if 300 <= y <= 400 or 700 <= y <= 800:
                return Vector(1, 0)
        return Vector(0, 1)


class DroitDevant(Path):
    @staticmethod
    def path(x, y):
        return Vector(0, 1)
