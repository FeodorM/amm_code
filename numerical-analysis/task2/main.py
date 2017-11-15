from math import exp

from typing import Callable, List


def runge_kutta(f: Callable[[float, float], float], y: float, a: float = 1, b: float = 2, h: float = 0.1
    ) -> List[float]:
    n = int(((b - a) / h))
    xs = [a + i * h for i in range(n)]
    ys = [y]
    for x in xs:
        k1 = h * f(x, y)
        k2 = h * f(x + h / 3, y + k1 / 3)
        k3 = h * f(x + 2 * h / 3, y + 2 * k2 / 3)
        y = y + (k1 + 3 * k3) / 4
        ys.append(y)
    return ys


# def runge_kutta_back(f: Callable[[float, float], float], y: float, a: float = 1, b: float = 2, h: float = 0.1) -> List[float]:
#     n = int(((b - a) / h))
#     xs = [a + i * h for i in range(1, n + 1)]
#     ys = [y]
#     h = -h
#     for x in reversed(xs):
#         k1 = h * f(x, y)
#         k2 = h * f(x + h / 3, y + k1 / 3)
#         k3 = h * f(x + 2 * h / 3, y + 2 * k2 / 3)
#         y = y + (k1 + 3 * k3) / 4
#         ys.insert(0, y)
#     return ys


def bla1():
    a, b = 1, 2
    h1 = 0.1
    h2 = h1 / 2
    # f = lambda x, y: 4 * x**3 + 4 * x + 5
    # ff = lambda x: x**4 + 2 * x**2 + 5 * x + 3
    # f = lambda x, y: 3 * x**2 + 4 * x + 5
    # ff = lambda x: x**3 + 2 * x**2 + 5 * x + 3
    # f = lambda x, y: 2 * x
    # ff = lambda x: x ** 2
    f = lambda x, y: -y
    ff = lambda x: exp(-x)
    y0 = ff(a)

    res1 = runge_kutta(
        f, y0, a, b, h1
    )[-1]
    res2 = runge_kutta(
        f, y0, a, b, h2
    )[-1]
    print("Точное значение: {}\n".format(ff(b)))
    print("Значение в точке {} с шагом {}: {}\nПогрешность: {}\n".format(b, h1, res1, res1 - ff(b)))
    print("Значение в точке {} с шагом {}: {}\nПогрешность: {}  ".format(b, h2, res2, res2 - ff(b)))


def bla2():
    a, b = 1, 2
    h1 = 0.1
    h2 = h1 / 2
    # f = lambda x, y: 4 * x**3 + 4 * x + 5
    # ff = lambda x: x**4 + 2 * x**2 + 5 * x + 3
    # f = lambda x, y: 3 * x**2 + 4 * x + 5
    # ff = lambda x: x**3 + 2 * x**2 + 5 * x + 3
    f = lambda x, y: 2 * x
    ff = lambda x: x ** 2
    # f = lambda x, y: -y
    # ff = lambda x: exp(-x)
    y0 = ff(b)

    res1 = runge_kutta_back(
        f, y0, a, b, h1
    )[0]
    res2 = runge_kutta_back(
        f, y0, a, b, h2
    )[0]
    print("Точное значение: {}\n".format(ff(a)))
    print("Значение в точке {} с шагом {}: {}\nПогрешность: {}\n".format(a, h1, res1, res1 - ff(a)))
    print("Значение в точке {} с шагом {}: {}\nПогрешность: {}  ".format(a, h2, res2, res2 - ff(a)))


if __name__ == '__main__':
    bla2()
