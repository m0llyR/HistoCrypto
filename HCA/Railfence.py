# -*- coding: utf-8 -*-

"""  Part of HCA - Historical Crypto Algorithms - Not to be considered safe for encryption!

Implementation of the Rail Fence algorithm
https://en.wikipedia.org/wiki/Rail_fence_cipher

Thanks to (code elements stolen from):
 - A bloody impressive piece of code: https://exercism.io/tracks/python/exercises/rail-fence-cipher/solutions/8d7425bdbb844c5e9416015cd7eb3daa
"""


from itertools import cycle


def rail_pattern(n):
    r = list(range(n))
    return cycle(r + r[-2:0:-1])


def encrypt(plaintext, rails):
    p = rail_pattern(rails)
    # this relies on key being called in order, guaranteed?
    return ''.join(sorted(plaintext, key=lambda i: next(p)))


def decrypt(ciphertext, rails):
    p = rail_pattern(rails)
    indexes = sorted(range(len(ciphertext)), key=lambda i: next(p))
    result = [''] * len(ciphertext)
    for i, c in zip(indexes, ciphertext):
        result[i] = c
    return ''.join(result)