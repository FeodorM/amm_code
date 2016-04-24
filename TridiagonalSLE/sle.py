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
    def from_file(file_name, as_matrix=False):
        """
        Read tridiagonal matrix from file.
        If as_matrix is Fasle,
        read 3 lines and interprete them as a, b, c vectors.
        Oterwise, read whole matrix, but then take just a, b, c from it.
        """
        with open(file_name) as file:
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
                    for i in range(1, len(x) - 1)] +
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
        pass


class TridiagonalMatrix_:
    """
    TridiagonalMatrix --- matrix with three diagonals,
    every other element is zero

    """
    def __init__(self, a, b, c):
        a[0] = 0
        c[-1] = 0
        self.lines = zip(a, b, c)

    def __len__(self):
        return len(self.lines)

    @staticmethod
    def random(size):
        """
        Return random tridiagonal matrix of given size
        """
        return TridiagonalMatrix_(*[Vector.random(size) for _ in range(3)])

    @staticmethod
    def from_file(file_name, as_matrix=False):
        """
        Read tridiagonal matrix from file.
        If as_matrix is Fasle,
        read 3 lines and interprete them as a, b, c vectors.
        Oterwise, read whole matrix, but then take just a, b, c from it.
        """
        with open(file_name) as file:
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
                [self.lines[0][1] * other[0] + self.lines[0][2] * other[1]] +
                [a * other[i - 1] +
                 b * other[i] +
                 c * other[i + 1]
                    for (a, b, c), i in zip(self.lines[1:-1], range(1, len(self) - 1))] +
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
        pass
