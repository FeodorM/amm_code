from random import random

class Vector(list):
    """Just mathematical vector"""

    @staticmethod
    def random(size):
        """Random vector of given size"""
        return Vector(random() * 50 for _ in range(size))

    @staticmethod
    def from_file(file):
        """Read a line from file and interprete it as vector"""
        return Vector(float(x) for x in file.readline().split())

    def __repr__(self):
        return "Vector({})".format(list.__repr__(self))

    def __str__(self):
        return '[ ' + '  '.join(str(round(x, 2)) for x in self) + ' ]'

    def __add__(self, other):
        assert len(self) == len(other), "Vectors should have same size"
        return Vector(x + y for x, y in zip(self, other))

    def __sub__(self, other):
        return self + (-other)

    def __neg__(self):
        return Vector(-x for x in self)

    def dot(self, other):
        """Dot (scalar) product"""
        assert len(self) == len(other), "Vectors should have same size"
        return sum(x * y for x, y in zip(self, other))

    def __abs__(self):
        return max(abs(x) for x in self)

    norm = __abs__

if __name__ == '__main__':
    v = Vector.random(10)
    print(repr(v))
