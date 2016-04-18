from numpy import *
from cmlib import showMatr

A = matrix([[1, 2, 0],
            [0, 2, 2]])
B = matrix([[3, -1],
            [-1, 3],
            [1, 0]])
res = (A * B).T
showMatr(array(res))
