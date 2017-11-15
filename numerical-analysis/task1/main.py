#!/usr/bin/env python3

import sys

# костыль для нормального импортирования остальных модулей при запуске из консоли
# когда-нибудь я найду способ получше
# просто закомментирте эту строку
sys.path.append('/home/fedor/code/amm_code/numerical-analysis')

from typing import Sequence, Callable, List

from matplotlib.patches import Patch
from matplotlib.pyplot import plot, show, legend, savefig, title

from utils.utils import parse, create_xs
from tabulate import tabulate
from random import choice


colors = ['red', 'green', 'blue', 'black']


def draw(xs: Sequence, arr, t, f) -> None:
    # legend(loc='upper center', shadow=True, fontsize='x-large')
    for (func, _), color in zip(arr, colors):
        plot(xs, func, color=color)
    legend(handles=[
        Patch(color=color, label='${}$'.format(name))
        for (_, name), color in zip(arr, colors)
    ])
    title(t)
    savefig(f + '.png')


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

def phi(v, x, z_, y_, h):
    a = y_ + h * v / x + 2 * v - 1
    b = y_ + h * v / x - 1
    return v - z_ - h * v / x * a / b


def phi_der(v, x, z_, y_, h):
    a = (y_ + h / x * v + 2 * v - 1) / (y_ + h * v / x - 1)
    b = (2 + h / x - h / x) / (y_ + h * v / x - 1) ** 2
    return 1 - h / x * a + h * v / x * b


def newton(x, y_, z_, h, eps):
    v_prev = z_
    count = 0
    while count < 1000000:
        count += 1
        v = v_prev - phi(v_prev, x, z_, y_, h) / phi_der(v_prev, x, z_, y_, h)
        # print(v_prev, v)
        if abs(v_prev - v) <= eps:
            break
        v_prev = v

    y = y_ + h * v / x
    # print(count)
    return y, v, count

def implicit_euler(n, a, b, y0, z0, eps):
    h = (b - a) / n
    xs = [a + i * h for i in range(n)]
    ys = [y0]
    zs = [z0]
    counts = []

    for x in xs:
        # y = ys[-1] + h * f1(x, ys[-1], zs[-1])
        # z = zs[-1] + h * f2(x, ys[-1], zs[-1])
        y, z, count = newton(x, ys[-1], zs[-1], h, eps)
        ys.append(y)
        zs.append(z)
        counts.append(count)
    return ys, zs, sum(counts) / len(counts)

def print_implicit(a, b, y0, z0, y_true, z_true):
    table = []
    for n in n_range:
        for eps in epss:
            ys, zs, count = implicit_euler(n, a, b, y0, z0, eps)
            xs = create_xs(a, b, n)
            y = [y_true(x) for x in xs]
            z = [z_true(x) for x in xs]
            y_error = [abs(y1 - y2) for y1, y2 in zip(ys, y)]
            z_error = [abs(z1 - z2) for z1, z2 in zip(zs, z)]
            table.append([
                n,
                eps,
                sum(y_error) / len(y_error),
                sum(z_error) / len(z_error),
                round(count)
            ])
    print(tabulate(table, headers=['n', 'eps', 'y err', 'z err', 'newton count']))


def print_explicit(a, b, y0, z0, y_der, z_der, y_true, z_true):
    table = []
    for n in n_range:
        ys, zs = euler(n, a, b, y0, z0, y_der, z_der)
        xs = create_xs(a, b, n)
        y = [y_true(x) for x in xs]
        z = [z_true(x) for x in xs]
        y_error = [abs(y1 - y2) for y1, y2 in zip(ys, y)]
        z_error = [abs(z1 - z2) for z1, z2 in zip(zs, z)]
        table.append([
            n,
            sum(y_error) / len(y_error),
            sum(z_error) / len(z_error)
        ])
    print(tabulate(table, headers=['n', 'y err', 'z err']))

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

    y_der = lambda x, y, z: z / x
    z_der = lambda x, y, z: z * (y + 2 * z - 1) / (x * (y - 1))
    y_true = lambda x: x / (x + 1)
    z_true = lambda x: x / (x + 1) ** 2

    # print_explicit(a, b, y0, z0, y_der, z_der, y_true, z_true)
    # print()
    # print_implicit(a, b, y0, z0, y_true, z_true)
    for n in n_range:
        if sys.argv[1] == "i":
            ys, zs, count = implicit_euler(n, a, b, y0, z0, choice(epss))
            t = "Неявный метод, N = " + str(n)
            f = "imp_" + str(n)
        else:
            ys, zs = euler(n, a, b, y0, z0, y_der, z_der)
            t = "Явный метод, N = " + str(n)
            f = "imp_" + str(n)


        xs = create_xs(a, b, n)
        y = [y_true(x) for x in xs]
        z = [z_true(x) for x in xs]

        res = [
            (ys, "y"),
            (zs, "z"),
            (y, "y(точный)"),
            (z, "z(точный)")
        ]
        draw(xs, res, t, f)
