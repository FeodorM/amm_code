import random
from merge_sorts import natural_merge_sort


class MatrixError(Exception):
    pass


# noinspection PyShadowingBuiltins
class Matrix:
    def __init__(self, matrix, type=float, already_good=False):
        if not already_good:
            self.matrix = [[type(x) for x in line] for line in matrix]
        else:
            self.matrix = matrix

    @staticmethod
    def from_file(file, type=float):
        first_row = list(map(type, file.readline().split()))
        if not first_row:
            return None
        m = len(first_row)
        matrix = [first_row] + [list(map(type, file.readline().split()))
                                for _ in range(m - 1)]
        return Matrix(matrix, type, already_good=True)

    def __str__(self):
        return '\n'.join(' '.join(map(str, line)) for line in self.matrix)

    __repr__ = __str__

    def __len__(self):
        return len(self.matrix)

    def __getitem__(self, item):
        return self.matrix[item]

    def __eq__(self, other):
        assert (isinstance(other, Matrix) and
                len(other) == len(self)
                )
        for i in range(len(self)):
            for j in range(len(self)):
                if self[i][j] != other[i][j]:
                    return False
        return True

    def key(self):
        res = 1
        for i in range(len(self.matrix)):
            res *= self.matrix[i][i]
        return res

    @staticmethod
    def random(dim=3):
        matrix = [[random.randint(1, 5) for _ in range(dim)]
                  for _ in range(dim)]
        return Matrix(matrix, int, already_good=True)

    @staticmethod
    def pretty_view(file_name, type=float):
        matrices = []
        sep = '*' * 15
        with open(file_name) as file:
            matr = Matrix.from_file(file, type)
            while matr is not None:
                matrices.append(matr)
                matr = Matrix.from_file(file, type)
        with open(file_name, 'w') as file:
            for matr in matrices:
                print(matr, file=file)
                print('Key: ', matr.key(), file=file)
                print(sep, file=file)


def create_some_random_matrices(file_name, number=5):
    with open(file_name, 'w') as file:
        for _ in range(number):
            print(Matrix.random(), file=file)


def copy_file(file_name, new_name):
    with open(file_name) as source, open(new_name, 'w') as target:
        target.write(source.read())


if __name__ == '__main__':
    create_some_random_matrices('source')
    copy_file('source', 'test')
    # test(lambda x: Matrix.from_file(x, int), key=Matrix.key)
    natural_merging_sort(
        'test',
        lambda x: Matrix.from_file(x, int),
        lambda x: -Matrix.key(x)
    )
    Matrix.pretty_view('source', int)
    Matrix.pretty_view('test', int)
