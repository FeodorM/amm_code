from random import random

class Vector:
    """Just mathematical vector"""
    def __init__(self, list_):
        self.list = list(list_)

	def __len__(self):
        return len(self.list)

    @staticmethod
    def random(size):
        """Random vector of given size"""
        return Vector(random() * 50 for _ in range(size))

    @staticmethod
    def from_file(file):
        """Read a line from file and interprete it as vector"""
        return Vector(float(x) for x in file.readline().split())

    def __repr__(self):
        return "Vector({})".format(
            ', '.join(str(x) for x in self.list))

    def __str__(self):
        return '\t'.join(str(x) for x in self.list)

    def __getitem__(self, index):
        return self.list[index]

    def __setitem__(self, index, value):
        self.list[index] = value

    def __add__(self, other):
        assert len(self) == len(other), "Vectors should have same size"
        return Vector(x + y for x, y in zip(self.list, other.list))

    def __sub__(self, other):
        return self + (-other)

    def __neg__(self):
        return Vector(-x for x in self.list)

    def dot(self, other):
        """Dot (scalar) product"""
        assert len(self) == len(other), "Vectors should have same size"
        return sum(x * y for x, y in zip(self.list, other.list))
