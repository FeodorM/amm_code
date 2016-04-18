import os


def end_of_file(file):
    cur = file.tell()
    if cur == file.seek(0, 2):
        return True
    file.seek(cur)
    return False


def read_next_int(file):
    res = file.readline()
    return int(res) if res != '' else None


def end_of_run(file):
    if file.read(1) != "'":
        file.seek(file.tell() - 1)
        return False
    return True


# noinspection PyAttributeOutsideInit
class File:
    def __init__(self, *args, **kwargs):
        self.file = open(*args, **kwargs)

    def __getattr__(self, item):
        return getattr(self.file, item)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


def natural_merge_sort(file_name, read, key=lambda x: x):
    flags = [True, True]
    while all(flags):
        flags = [False, False]
        f = open(file_name)
        sup = tuple(open('sup{}'.format(i), 'w') for i in range(2))
        current = False

        first = read(f)
        if not end_of_file(f):
            print(first, file=sup[current])
        while not end_of_file(f):
            second = read(f)
            # noinspection PyUnboundLocalVariable
            if key(second) < key(first):
                print("'", end='', file=sup[current])
                flags[current] = True
                current = not current
            print(second, file=sup[current])
            flags[current] = True
            first = second

        if flags[current]:
            print("'", end='', file=sup[current])

        for file in (f,) + sup:
            file.close()

        f = open(file_name, 'w')
        f1, f2 = [open('sup{}'.format(i)) for i in range(2)]

        if not end_of_file(f1):
            first = read(f1)
        if not end_of_file(f2):
            second = read(f2)
        while not end_of_file(f1) and not end_of_file(f2):
            file1 = file2 = False
            while not file1 and not file2:
                # noinspection PyUnboundLocalVariable
                if key(first) < key(second):
                    print(first, file=f)
                    file1 = end_of_run(f1)
                    first = read(f1)
                else:
                    print(second, file=f)
                    file2 = end_of_run(f2)
                    second = read(f2)
            while not file1:
                print(first, file=f)
                file1 = end_of_run(f1)
                first = read(f1)
            while not file2:
                print(second, file=f)
                file2 = end_of_run(f2)
                second = read(f2)
        file1 = file2 = False
        while not file1 and not end_of_file(f1):
            print(first, file=f)
            file1 = end_of_run(f1)
            first = read(f1)
        while not file2 and not end_of_file(f2):
            print(second, file=f)
            file2 = end_of_run(f2)
            second = read(f2)

        for file in f, f1, f2:
            file.close()

    os.remove("sup0")
    os.remove("sup1")


# noinspection PyShadowingNames,PyTypeChecker
def strange_merge_sort(file_name, number, read, key=lambda x: x):
    assert number >= 2, "Number must be greater than 1."

    flags = [True] * number
    while len([flag for flag in flags if flag]) > 1:
        flags = [False] * number
        f = open(file_name)
        sup = tuple((open('sup{}'.format(x), 'w') for x in range(number)))
        current = 0

        first = read(f)
        if not end_of_file(f):
            print(first, file=sup[current])
        while not end_of_file(f):
            second = read(f)
            if key(second) < key(first):
                print("'", end='', file=sup[current])
                flags[current] = True
                current += 1
                if current == number:
                    current = 0
            print(second, file=sup[current])
            flags[current] = True
            first = second

        if flags[current]:
            print("'", end='', file=sup[current])

        for file in (f,) + sup:
            file.close()

        f = open(file_name, 'w')
        sup = [File('sup{}'.format(x)) for x in range(number)]

        for file in sup:
            if not end_of_file(file):
                file.value = read(file)

        not_empty_files = [file for file in sup if not end_of_file(file)]

        while not_empty_files:
            current_files = list(not_empty_files)
            while current_files:
                file = min(current_files, key=lambda file: key(file.value))
                print(file.value, file=f)
                if end_of_run(file):
                    current_files.remove(file)
                file.value = read(file)
            not_empty_files = [file for file in not_empty_files
                               if not end_of_file(file)]

        for file in [f] + sup:
            file.close()

    for x in range(number):
        os.remove('sup{}'.format(x))


def test():
    from random import randint
    from tqdm import tqdm

    for _ in tqdm(range(100)):
        run = [randint(0, 10) for _ in range(100)]

        open('f1', 'w').write('\n'.join(map(str, run)))
        open('f2', 'w').write('\n'.join(map(str, run)))

        natural_merge_sort('f1', read_next_int)
        strange_merge_sort('f2', randint(2, 50), read_next_int)

        t1 = list(map(int, open('f1').read().split()))
        t2 = list(map(int, open('f2').read().split()))

        assert t1 == t2

    os.remove('f1')
    os.remove('f2')


if __name__ == '__main__':
    test()
