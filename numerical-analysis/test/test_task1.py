from unittest import TestCase

from task1.main import euler
from utils.utils import create_xs


class TestTask1(TestCase):
    funcs = [
        (10, 1, 2, 1, 1,
         lambda x, y, z: 1,
         lambda x, y, z: 1,
         lambda x: x,
         lambda x: x),
        (100, 1, 2, 1, 1,
         lambda x, y, z: 1,
         lambda x, y, z: 1,
         lambda x: x,
         lambda x: x)
        # TODO: test cases
    ]

    # TODO: not so ugly tests
    def test_euler(self):
        for n, a, b, y0, z0, yd, zd, y_etalon, z_etalon in self.funcs:
            xs = create_xs(a, b, n)
            ys, zs = euler(n, a, b, y0, z0, yd, zd)
            ys_etalon = [y_etalon(x) for x in xs]
            zs_etalon = [z_etalon(x) for x in xs]
            assert all(abs(y - y_e) < 0.000001 for y, y_e in zip(ys, ys_etalon))
            assert all(abs(z - z_e) < 0.000001 for z, z_e in zip(zs, zs_etalon))
