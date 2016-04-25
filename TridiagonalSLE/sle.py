#!/usr/bin/env python3
from vector import Vector

class TridiagonalMatrix:
    """
    TridiagonalMatrix --- matrix with three diagonals,
    every other element is zero

    """
    def __init__(self, a, b, c):
        self.a, self.b, self.c = [Vector(x) for x in (a, b, c)]
        self.a[0]  = 0
        self.c[-1] = 0

    def __len__(self):
        return len(self.b)

    @staticmethod
    def random(size):
        """
        Return random tridiagonal matrix of given size
        """
        return TridiagonalMatrix(*[Vector.random(size) for _ in range(3)])

    @staticmethod
    def from_file(file, as_matrix=False):
        """
        Read tridiagonal matrix from file.
        If as_matrix is Fasle,
        read 3 lines and interprete them as a, b, c vectors.
        Oterwise, read whole matrix, but then take just a, b, c from it.
        """
        if as_matrix:
            matrix = [[float(x) for x in line.split()] for line in file]
            return TridiagonalMatrix(
                [0] + [matrix[i + 1][i] for i in range(len(matrix) - 1)],
                [matrix[i][i] for i in range(len(matrix))],
                [matrix[i][i + 1] for i in range(len(matrix) - 1)] + [0]
            )
        else:
            return TridiagonalMatrix(*[Vector.from_file(file)
                                        for _ in range(3)])

    def __repr__(self):
        return "TridiagonalMatrix({self.a}\n{i}{self.b}\n{i}{self.c}".format(
            i="                  ",
            self=self
        )

    def __str__(self):
        return '\n'.join(
            '\t'.join(str(round(x, 3)) for x in line)
                for line in self.matrix()
        )

    @staticmethod
    def _zeros(n):
        return [0] * n

    def matrix(self):
        """
        Return representation of self as a matrix
        """
        size = len(self) - 2
        zeros = self._zeros
        middle = [
            zeros(i - 1) + [a, b, c] + zeros(size - i)
                for i, (a, b, c) in enumerate(
                    zip(self.a[1:], self.b[1:], self.c[1:-1]), 1
                )
        ]
        return (
            [self.b[:1] + self.c[0:1] + [0] * (len(self) - 2)] +
            middle +
            [[0] * (len(self) - 2) + self.a[-1:] + self.b[-1:]]
        )

    def __add__(self, other):
        assert len(self) == len(other), "Matrices should have same size"
        return TridiagonalMatrix(
            [x + y for x, y in zip(self.a, other.a)],
            [x + y for x, y in zip(self.b, other.b)],
            [x + y for x, y in zip(self.c, other.c)]
        )

    def __neg__(self):
        return TridiagonalMatrix(
            [-x for x in self.a],
            [-x for x in self.b],
            [-x for x in self.c]
        )

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other):
        """
        Matrix product with tridiagonal matrix or vector
        """
        assert len(self) == len(other), "Matrices should have same size"
        if isinstance(other, TridiagonalMatrix):
            pass
        elif isinstance(other, Vector):
            return Vector(
                [self.b[0] * other[0] + self.c[0] * other[1]] +
                [self.a[i] * other[i - 1] +
                 self.b[i] * other[i] +
                 self.c[i] * other[i + 1]
                    for i in range(1, len(other) - 1)] +
                [self.a[-1] * other[-2] + self.b[-1] * other[-1]]
            )
        raise TypeError(
            "Wring type for multiplication: {}".format(other.__class__)
        )

    def linsolve(self, vector):
        """
        Solve SLE $Ax = vector$
        return x
        """
        assert len(self) == len(vector), "Vector and matrix should have same size"
        ls = [0]
        ms = [0]
        for a, b, c, d in zip(self.a, self.b, self.c, vector):
            ms.append((d - a * ms[-1]) / (b - a * ls[-1]))
            ls.append(c / (b - a * ls[-1]))
        ls.pop()
        ls.pop(0)
        ms.pop(0)
        x = [ms.pop()]
        for l, m in zip(reversed(ls), reversed(ms)):
            x.append(m - l * x[-1])
        return Vector(reversed(x))

    def unstable_linsolve(self, vector):
        """
        Solve SLE $Ax = vector$
        return x
        BUT!
        Solve it with unstable method,
        that sometimes works surprisingly (for me) bad. Realy bad.
        """
        assert len(self) == len(vector), "Vector and matrix should have same size"
        y = [0, vector[0] / self.c[0]]
        z = [1, - self.b[0] / self.c[0]]
        for a, b, c, d in zip(self.a[1:-1], self.b[1:], self.c[1:], vector[1:]):
            y.append((d - a * y[-2] - b * y[-1]) / c)
            z.append(-(a * z[-2] + b * z[-1]) / c)
        k = ((vector[-1] - self.a[-1] * y[-2] - self.b[-1] * y[-1]) /
             (self.a[-1] * z[-2] + self.b[-1] * z[-1]))
        return Vector(y + k * z for y, z in zip(y, z))



if __name__ == '__main__':
    # with open('test') as file:
    #     m = TridiagonalMatrix.from_file(file)
    #     v = Vector.from_file(file)
    size = 100
    m        = TridiagonalMatrix.random(size)
    x        = Vector.random(size)
    d        = m * x
    solution = m.unstable_linsolve(d)
    for a, b in zip(x, solution):
        print(a, b, sep='\t')
    print((abs(x - solution)))
