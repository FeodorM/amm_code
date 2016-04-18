from numpy import *
from numpy import linalg as l
from cmlib import showMatr


def make_ort(matr):
    """

    :param matr: ndarray, rows - vectors to ort***
    :return: nothing... it's just orthogonalizing
    """
    for i in range(matr.shape[0]):
        summ = matr[i]
        for j in range(i):
            summ -= dot(matr[i], matr[j]) / dot(matr[j], matr[j]) * matr[j]
        matr[i] = summ


a = array([[1, 1, 1, 1],
           [3, 3, -1, -1],
           [-2, 0, 6, 8]], dtype='float64')
print(a)
make_ort(a)
# print(a)
showMatr(a)
