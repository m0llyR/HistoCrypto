# -*- coding: utf-8 -*-

""" Part of HCA - Historical Crypto Algorithms - Not to be considered safe for encryption!

Implementation of the Vernam Cipher in Cryptography
https://www.geeksforgeeks.org/vernam-cipher-in-cryptography/

Thanks to (code elements stolen from):
 - https://www.geeksforgeeks.org/vernam-cipher-in-cryptography/


Vernam Cipher is a method of encrypting alphabetic text. It is simply a type of substitution cipher.
In this mechanism we assign a number to each character of the Plain-Text, like (a = 0, b = 1, c = 2, … z = 25).

Method to take key:
In Vernam cipher algorithm, we take a key to encrypt the plain text which length should be equal to the length of the
plain text.

Encryption Algorithm:

    Assign a number to each character of the plain-text and the key according to alphabetic order.
    Add both the number (Corresponding plain-text character number and Key character number).
    Subtract the number from 26 if the added number is grater than 26. otherwise leave it.

Example:

Plain-Text: RAMSWARUPK
Key: RANCHOBABA

Now according to our encryption algorithm we assign a number to each character of our plain-text and key.

PT:   R  A  M   S   W   A  R   U   P   K
NO:   17 0  12  18  22  0  17  20  15  10

KEY:  R   A  N   C  H  O   B  A  B  A
NO:   17  0  13  2  7  14  1  0  1  0

Now add the number of Plain-Text and Key and after doing the addition and subtraction operation (if required), we will
get the corresponding Cipher-Text character number.

CT-NO: 34  0  25  20  29  14  18  20  16  10

In this case, there are two numbers which are greater than the 26, so we have to subtract 26 from them and after
applying the subtraction operation the new Cipher text character numbers are as follows:

CT-NO:  8  0  25   20   3   14   18   20   16   10

New Cipher-Text is after getting the corresponding character from the number.

CIPHER-TEXT: I  A  Z  U  D  O  S  U  Q  K

Note:
For the Decryption; just reverse process of encryption.
"""

import random


def generate_key(plaintext_length):
    key = ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(plaintext_length))
    return key


def encrypt(plaintext, key):
    ciphertext = ''.join(chr(ord(p) ^ ord(k)) for p, k in zip(plaintext, key))
    return ciphertext


def decrypt(ciphertext, key):
    decrypted_text = ''.join(chr(ord(c) ^ ord(k)) for c, k in zip(ciphertext, key))
    return decrypted_text


# Example usage
if __name__ == "__main__":
    plaintext = "HELLO"
    key = generate_key(len(plaintext))

    print("Plaintext:", plaintext)
    print("Key:", key)

    ciphertext = encrypt(plaintext, key)
    print("Ciphertext:", ciphertext)

    decrypted_text = decrypt(ciphertext, key)
    print("Decrypted Text:", decrypted_text)
