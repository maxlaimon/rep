import math

class Vector:

    def __init__(self, inpstr):
        inp = list(map(float, inpstr.split(',')))

        self.x = inp[0]
        self.y = inp[1]
        self.z = inp[2]

    def __str__(self):
        return f'({self.x}, {self.y}, {self.z})'

    def __add__(self, other):
        return Vector(f'{self.x + other.x}, {self.y + other.y}, {self.z + other.z}')

    def __sub__(self, other):
        return Vector(f'{self.x - other.x}, {self.y - other.y}, {self.z - other.z}')

    def __and__(self, other):
        return Vector(f'{self.y*other.z - other.y*self.z}, {other.x*self.z - self.x*other.z}, {self.x*other.y - self.y*other.x}')

    def distance(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
