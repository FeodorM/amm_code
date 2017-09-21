from math import *
from typing import Callable


# TODO: docs
def parse(expr: str, args) -> Callable[[float, float, float], float]:
    return eval("lambda {}: {}".format(args, expr))


def create_xs(a, b, n):
    h = (b - a) / n
    return [a + i * h for i in range(n + 1)]
