#!/usr/bin/env python3

import sys

# костыль для нормального импортирования остальных модулей при запуске из консоли
# когда-нибудь я найду способ получше
# просто закомментирте эту строку
sys.path.append('/home/satan/code/amm/numerical-analysis')

from typing import Sequence, Callable, List

from matplotlib.patches import Patch
from matplotlib.pyplot import plot, show, legend

from utils.utils import parse, create_xs


colors = ['red', 'green', 'blue', 'black']


def draw(xs: Sequence, arr) -> None:
    # legend(loc='upper center', shadow=True, fontsize='x-large')
    for func, _ in arr:
        plot(xs, func)
    legend(handles=[
        Patch(color=color, label='${}$'.format(name))
        for (_, name), color in zip(arr, colors)
    ])
    show()


def euler(n: int, a: int, b: int, y0: float, z0: float,
          f1: Callable[[float, float, float], float],
          f2: Callable[[float, float, float], float]
          ) -> (List[float], List[float]):
    """
    TODO
    :param n: number of intervals (there will be (n + 1) points in mesh)
    :param a: left boundary
    :param b: right boundary
    :param y0: y(a) = y0
    :param z0: z(a) = z0
    :param f1: y' = f1
    :param f2: z' = f2
    :return: ys, zs --- values of functions y and z on mesh xs
    """
    h = (b - a) / n
    xs = [a + i * h for i in range(n)]
    ys = [y0]
    zs = [z0]

    for x in xs:
        y = ys[-1] + h * f1(x, ys[-1], zs[-1])
        z = zs[-1] + h * f2(x, ys[-1], zs[-1])
        ys.append(y)
        zs.append(z)
    return ys, zs


if __name__ == '__main__':
    def get_func(text: str, args) -> (Callable[[float, float, float], float], str):
        func_str = input(text)
        {
            "y' = ": "our func"
            "z' = ": "our func"
            "y = ": "etalon"
            "z = ": "etalon"
        }
        return parse(func_str, args), func_str


    n = int(input("n = "))
    a = 1 #int(input("a (left boundary) = "))
    b = 2 #int(input("b (right boundary) = "))
    y0 = float(input("y(a) = "))
    z0 = float(input("z(a) = "))
    funcs = [get_func(text, "x, y, z") for text in ("y' = ", "z' = ")] + \
            [get_func(text, "x") for text in ("y = ", "z = ")]
    yz = euler(n, a, b, y0, z0, funcs[0][0], funcs[1][0])
    xs = create_xs(a, b, n)
    y = [funcs[2][0](x) for x in xs]
    z = [funcs[3][0](x) for x in xs]
    res = [
        (yz[0], funcs[0][1]),
        (yz[1], funcs[1][1]),
        (y, funcs[2][1]),
        (z, funcs[3][1])
    ]
    draw(xs, res)
