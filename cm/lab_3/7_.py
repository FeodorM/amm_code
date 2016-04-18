from numpy import *
from numpy import linalg as l
from cmlib import showMatr


def is_in_linear_span(matr, vect):
    """

    :param matr: system of vectors MxN
    :param vect: just a vector, matrix with shape 1xN
    :return: True if vect is in linear span of vectors-rows of matr
    """
    return l.matrix_rank(matr) == l.matrix_rank(vstack((matr, vect)))


x = matrix([[2, 1, 4, -2],
            [1, 2, 3, -1],
            [1, 0, 1, -1]])
y = matrix([3, 2, 1, 0])
print(is_in_linear_span(x, y))
# print(l.matrix_rank(x) == l.matrix_rank(vstack((x, y))))
