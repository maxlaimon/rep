import math

class Vector:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f'({self.x}, {self.y}, {self.z})'

    def __add__(self, other):
        return Vector({self.x + other.x}, {self.y + other.y}, {self.z + other.z})

    def __sub__(self, other):
        return Vector({self.x - other.x}, {self.y - other.y}, {self.z - other.z})

    def __and__(self, other):
        return Vector({self.y*other.z - other.y*self.z}, {other.x*self.z - self.x*other.z}, {self.x*other.y - self.y*other.x})

    def distance(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
