from numpy import *
from numpy import linalg as l
from fractions import Fraction
from cmlib import showMatr

a = array([1, 2, 0])
b = array([2, 0, -1])
ang = dot(a, b) / (l.norm(a) * l.norm(b))
print(Fraction(str(ang)))
showMatr([[Fraction(str(ang))]])
