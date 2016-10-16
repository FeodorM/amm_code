#! /usr/bin/env python3

import math
import decimal


n = 26


def forward():
    # j = [math.exp(-1)]
    # for i in range(2, n + 1):
    #     j.append(1 - i * j[-1])

    j = [decimal.Decimal(-1).exp()]
    for i in range(2, n + 1):
        j.append(1 - i * j[-1])

    for i in range(len(j)):
        print(i + 1, j[i], sep='\t')


def backward():
    l = 100
    j = [0] * l
    for i in range(l - 2, -1, -1):
        j[i] = (1 - j[i + 1]) / (i + 1)
    print(j[1] - math.exp(-1))
    print(*enumerate(j), sep='\n')


if __name__ == '__main__':
    backward()
