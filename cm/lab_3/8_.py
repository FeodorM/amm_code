from numpy import *
from numpy import linalg as l
from cmlib import showMatr

A_e = array([[15, -11, 5],
             [20, -15, 8],
             [8, - 7, 6]])
f_1 = array([2, 3, 1])
f_2 = array([3, 4, 1])
f_3 = array([1, 2, 2])

s_ef = vstack((f_1, f_2, f_3)).T

A_f = dot(dot(l.inv(s_ef), A_e), s_ef)

A_f = array([[int(round(elem)) for elem in row] for row in A_f])

showMatr(A_f)
