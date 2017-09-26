from math import *
from typing import Callable, List


def parse(expr: str, args: str) -> Callable[[float, float, float], float]:
    """
    Parse function from string
    :param expr: string, containing function expression. Just expression.
        It can contain fny variable from args and any math function (from Python's math module)
    :param args: list of variables in form of "x, y, z"
    :return: anonymous function -- lambda args: expr
    """
    return eval("lambda {}: {}".format(args, expr))


def create_xs(a: float, b: float, n: int) -> List[float]:
    """
    Create mesh with step h = (b - a) / n and boundaries a and b.
    :param a: left boundary
    :param b: right boundary
    :param n: number of subintervals
    :return: list of floats
    """
    h = (b - a) / n
    return [a + i * h for i in range(n + 1)]
