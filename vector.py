from math import sqrt

class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def norm(self):
        return sqrt(self.x ** 2 + self.y ** 2)

    def __rmul__(self, other):
        return Vector(other * self.x, other * self.y)
