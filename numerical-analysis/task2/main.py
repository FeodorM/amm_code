#!/usr/bin/env python3

import sys

sys.path.append('/home/fedor/code/amm_code/numerical-analysis')

from math import exp

from typing import Callable, List

from utils.draw import draw
from utils.utils import create_xs


def runge_kutta(
        f: Callable[[float, float], float],
        y: float,
        a: float = 1,
        b: float = 2,
        h: float = 0.1
    ) -> List[float]:
    n = int(((b - a) / h))
    xs = [a + i * h for i in range(n)]
    ys = [y]
    for x in xs:
        k1 = h * f(x, y)
        k2 = h * f(x + h / 2, y + k1 / 2)
        k3 = h * f(x + h / 2, y + k2 / 2)
        k4 = h * f(x + h, y + k3)
        y = y + (k1 + 2 * k2 + 2 * k3 + k4) / 6
        ys.append(y)
    return ys

def runge_kutta_system(f, g, y, z, a, b, n):
    h = (b - a) / n
    xs = [a + i * h for i in range(n)]
    ys = [y]
    zs = [z]

    for x in xs:
        k11 = h * f(x, y, z)
        k12 = h * g(x, y, z)

        k21 = h * f(x + h / 2, y + k11 / 2, z + k12 / 2)
        k22 = h * g(x + h / 2, y + k11 / 2, z + k12 / 2)

        k31 = h * f(x + h / 2, y + k21 / 2, z + k22 / 2)
        k32 = h * g(x + h / 2, y + k21 / 2, z + k22 / 2)

        k41 = h * f(x + h, y + k31, z + k32)
        k42 = h * g(x + h, y + k31, z + k32)

        y = y + (k11 + 2 * k21 + 2 * k31 + k41) / 6
        z = z + (k12 + 2 * k22 + 2 * k32 + k42) / 6

        ys.append(y)
        zs.append(z)
    return ys, zs

def test():
    a, b = 1, 2
    h1 = 0.1
    f = lambda x, y, z: z / x
    g = lambda x, y, z: z * (y + 2 * z - 1) / (x * (y - 1))

    y_true = lambda x: x / (x + 1)
    z_true = lambda x: x / (x + 1) ** 2

    # y0 = ff(a)
    y0 = 1/2
    z0 = 1/4

    ys, zs = runge_kutta_system(
        f, y0, a, b, h1
    )

    print("Точное значение: {}\n".format(ff(b)))
    print("Значение в точке {} с шагом {}: {}\nПогрешность: {}\n".format(b, h1, res1, res1 - ff(b)))
    print("Значение в точке {} с шагом {}: {}\nПогрешность: {}  ".format(b, h2, res2, res2 - ff(b)))


# y' = f(x, y, z)
# z' = g(x, y, z)
# y(x0) = y0
# z(x0) = z0

def print_charts():
    for n in n_range:
        ys, zs = runge_kutta_system(y_der, z_der, y0, z0, a, b, n)
        title = "N = " + str(n)
        file_name = "imp_" + str(n)

        xs = create_xs(a, b, n)
        y = [y_true(x) for x in xs]
        z = [z_true(x) for x in xs]

        # print(len(xs), len)
# 2, 4, 8, считать погрешности на правом конце отрезка, всё в таблицу. погрешность должна меняться в 2**4 раз
        res = [
            (ys, "y"),
            (zs, "z"),
            (y, "y(точный)"),
            (z, "z(точный)")
        ]

        draw(xs, res, title, file_name)


if __name__ == '__main__':
    def get_func(text: str, args) -> (Callable[[float, float, float], float], str):
        func_str = input(text)
        return parse(func_str, args), func_str

    import sys
    # n = int(sys.argv[1]) #int(input("n = "))
    a = 1 # int(input("a (left boundary) = "))
    b = 2 # int(input("b (right boundary) = "))
    y0 = 0.5 # float(input("y(a) = "))
    z0 = 0.25 #float(input("z(a) = "))

    epss = (0.1, 0.01, 0.001)
    n_range = (5, 10, 50, 100)
    n_range = (5, 50, 100)
    n_range = (2, 5, 10)

    y_der = lambda x, y, z: z / x
    z_der = lambda x, y, z: z * (y + 2 * z - 1) / (x * (y - 1))
    y_true = lambda x: x / (x + 1)
    z_true = lambda x: x / (x + 1) ** 2

    # print_explicit(a, b, y0, z0, y_der, z_der, y_true, z_true)
    # print()
    # print_implicit(a, b, y0, z0, y_true, z_true)
    print_charts()
