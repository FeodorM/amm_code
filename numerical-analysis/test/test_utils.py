from random import randint, random
from unittest import TestCase, skip

from math import cos, sin

from utils import parse


def rand_int():
    return randint(-100, 100)


def rand_float():
    return random() * rand_int()


rand = rand_float


class TestUtils(TestCase):

    xs = [(rand(), abs(rand()), rand()) for i in range(100)]

    funcs = [
        (lambda x, y, z: x + y + z, "x + y + z"),
        (lambda x, y, z: x * y * z, "x * y * z"),
        (lambda x, y, z: x * y - z * 10 + 123, "x * y - z * 10 + 123"),
        (lambda x, y, z: x ** y - cos(z) * x - sin(y), "x ** y - cos(z) * x - sin(y)")
    ]

    # @skip("why not")
    def test_parse(self):
        for func_etalon, func_str in self.funcs:
            func = parse(func_str, "x, y, z")
            assert all((
                x == y for x, y in zip(
                    (func(x, y, z) for x, y, z in self.xs),
                    (func_etalon(x, y, z) for x, y, z in self.xs)
                )
            ))
