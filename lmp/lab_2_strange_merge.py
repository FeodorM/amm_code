from random import randint, choice
from merge_sorts import strange_merge_sort
from string import ascii_letters
from lab_1_natural_merge import copy_file


def create_random_strings(number_of_strings=5, number_of_letters=(5, 7)):
    res = [
        ''.join(
            choice(ascii_letters) for _ in range(randint(*number_of_letters))
        ) for _ in range(number_of_strings)
    ]
    return res


if __name__ == '__main__':
    number_of_strings = 5
    open('sorted', 'w').write(
        '\n'.join(create_random_strings(number_of_strings)))
    copy_file('sorted', 'source')
    num = int(input('Enter number of files: '))
    assert 2 <= num <= number_of_strings
    strange_merge_sort(
        'sorted',
        num,
        lambda file: file.readline().strip(),
        lambda s: s[::-1]
    )
