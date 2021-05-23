from vector import Vector
from abc    import ABC, abstractmethod

class Path:
    @abstractmethod
    def path(x, y):
        pass

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
