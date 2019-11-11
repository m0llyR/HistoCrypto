# -*- coding: utf-8 -*-

""" Part of HCA - Historical Crypto Algorithms - Not to be considered safe for encryption!

Implementation of the Vigenère cipher algorithm
https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher

https://www.geeksforgeeks.org/vigenere-cipher/
https://rosettacode.org/wiki/Vigen%C3%A8re_cipher#Python

Thanks to (code elements stolen from):
-
"""



def rfe(keyword, start=0):
    """ Repeat for ever - looping over keyword """
    n = start
    while True:
        if n > len(keyword)-1: n = 0
        yield keyword[n]
        n += 1


def myencrypt(str_clear):
    str_cipher = ''

    return str_cipher


def mydecrypt(str_cipher):
    str_clear = ''

    return str_clear

keyw = rfe("abc")

for x in range(9):
    print(x, next(keyw))


'''Vigenere encryption and decryption'''

from itertools import starmap, cycle


def encrypt(message, key):
    '''Vigenere encryption of message using key.'''
    # Converted to uppercase.
    # Non-alpha characters stripped out.
    message = filter(str.isalpha, message.upper())
    def enc(c, k):
        '''Single letter encryption.'''
        return chr(((ord(k) + ord(c) - 2 * ord('A')) % 26) + ord('A'))
    return ''.join(starmap(enc, zip(message, cycle(key))))


def decrypt(message, key):
    '''Vigenere decryption of message using key.'''
    def dec(c, k):
        '''Single letter decryption.'''
        return chr(((ord(c) - ord(k) - 2 * ord('A')) % 26) + ord('A'))
    return ''.join(starmap(dec, zip(message, cycle(key))))


def main():
    '''Demonstration'''
    text = 'Beware the Jabberwock, my son! The jaws that bite, the claws that catch!'
    key = 'VIGENERECIPHER'
    encr = encrypt(text, key)
    decr = decrypt(encr, key)
    print("raw:", text)
    print("enc:", encr)
    print("dec:", decr)


if __name__ == '__main__':
    main()