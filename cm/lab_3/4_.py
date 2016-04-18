from numpy import *
from cmlib import showMatr

A = matrix([[1, 1, 2],
            [1, -2, -1],
            [2, 1, 3],
            [-1, 2, 1]])
print(A.shape)
showMatr(array(A))
print(linalg.matrix_rank(A) < A.shape[1])
