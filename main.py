#!/usr/bin/python
# -*- coding: utf-8 -*-

""" Main HCA caller ...
"""

import HCA.Caesar

# print(''.join([chr(n) for n in range(65, 91)]))  # upper case = [65..90]
# print(''.join([chr(n) for n in range(97, 123)]))  # lower case = [97..122]

rawt = "In there stepped a stately Raven of the saintly days of yore;"

# Caesar
s = 13
enct = HCA.Caesar.encrypt(rawt, s)
dect = HCA.Caesar.decrypt(enct, s)
print(f"Original: {rawt}\nCaesar  : {enct}\nDecrypt : {dect}")

# Vigenère