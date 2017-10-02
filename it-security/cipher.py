#!/usr/bin/env python3.6


# шифровка / дешифровка

from sys import argv

def chiper(string):
    return ''.join(cipher_dict[x] for x in string)

def dechipher(string):
    return ''.join(decipher_dict[x] for x in string)

s_from = "abcdefghijklmnopqrstuvwxyz"
s_to = "szfwldvghiytmxjqbkoncaerpu"
cipher_dict = dict(zip(s_from, s_to))
decipher_dict = dict(zip(s_to, s_from))

s = argv[1]

ciphered = chiper(s)
dechiphered = dechipher(ciphered)
print(f'input = "{s}"')
print(f'chiphered = "{ciphered}"')
print(f'dechiphered = "{dechiphered}"')
