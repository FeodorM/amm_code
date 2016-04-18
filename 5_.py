from numpy import *
from cmlib import showMatr


A = matrix([[1, 2],
            [3, 4]], dtype='int')
B = matrix([[3, 5],
            [5, 9]], dtype='int')
res = linalg.solve(A, B)
showMatr(array(res))
