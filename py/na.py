#! /usr/bin/python3

#numerical analysis

eps = 1
n = 0
beta = 2
while 1 + eps > 1:
    eps /= beta
    n += 1
eps *= beta
n -= 1

eps = 1
p = 1 + eps
m = 0
while p > 1:
    eps /= beta
    p = 1 + eps
    m += 1

m -= 1

print((
    'm: {}\n'
    'n: {}'
).format(m, n))
