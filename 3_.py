from numpy import *
from numpy import random
from cmlib import showMatr


def is_upper_triangular(matr):  # matrix as array with shape == (n, n)
    for i in range(len(matr)):
        for j in range(i):
            if matr[i][j] != 0:
                return False
    return True


a = random.randint(1, 10, (10, 10))
b = eye(10, 10, dtype='int')
showMatr(a)
print(is_upper_triangular(a))
showMatr(b)
print(is_upper_triangular(b))
