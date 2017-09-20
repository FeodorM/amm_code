#!/usr/bin/env python3.6

from sys import argv

def chiper(string):
    return ''.join(cipher_dict[x] for x in string)

def dechipher(string):
    return ''.join(decipher_dict[x] for x in string)


cipher_dict = dict(zip("abcdefghijklmnopqrstuvwxyz ", " abcdefghijklmnopqrstuvwxyz"))
decipher_dict = {v: k for k, v in cipher_dict.items()}

s = argv[1]

ciphered = chiper(s)
dechiphered = dechipher(ciphered)
print(f'input = "{s}"')
print(f'chiphered = "{ciphered}"')
print(f'dechiphered = "{dechiphered}"')
