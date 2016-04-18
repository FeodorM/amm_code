from numpy import *
from numpy import linalg as l
from cmlib import showMatr

a = matrix([[1, 1, 1],
            [1, 0, 3],
            [1, -1, 5]])
b = matrix([[1, 0, 3, 4],
            [2, 1, 4, 6],
            [3, 2, 5, 8]])
r = l.matrix_rank(a) == l.matrix_rank(hstack((a, b)))
print(r)
