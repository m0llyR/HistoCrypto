# -*- coding: utf-8 -*-

""" Part of HCA - Historical Crypto Algorithms - Not to be considered safe for encryption!

Implementation of the Caesar cipher algorithm
https://en.wikipedia.org/wiki/Caesar_cipher

Thanks to (code elements stolen from):
 - https://www.thecrazyprogrammer.com/2018/05/caesar-cipher-in-python.html
 - https://www.tutorialspoint.com/cryptography_with_python/cryptography_with_python_caesar_cipher.htm
 - https://www.geeksforgeeks.org/caesar-cipher-in-cryptography/
"""

import string


def encrypt(str_clear, int_shift):
    str_cipher = ''
    for chr_n in str_clear:
        if chr_n not in string.ascii_letters:  # Filtering <space> as well as ,.;:!? etc.
            str_cipher += chr_n
        elif chr_n.isupper():
            str_cipher += chr((ord(chr_n) + int_shift - 65) % 26 + 65)
        else:
            str_cipher += chr((ord(chr_n) + int_shift - 97) % 26 + 97)
    return str_cipher


def decrypt(str_cipher, int_shift):
    str_clear = ''
    for chr_n in str_cipher:
        if chr_n not in string.ascii_letters:  # Filtering <space> as well as ,.;:!? etc.
            str_clear += chr_n
        elif chr_n.isupper():
            str_clear += chr((ord(chr_n) - int_shift - 65) % 26 + 65)
        else:
            str_clear += chr((ord(chr_n) - int_shift - 97) % 26 + 97)
    return str_clear

