# -*- coding: utf-8 -*-

""" Part of SCA - Simple Crypto Attempts - Not to be considered safe for encryption!
simply using base64 encoding, as if it was an encryption - which it's not
And the = at the end is a dead giveaway...!
"""

import base64


def encrypt(str_clear):
    return base64.b64encode(str_clear.encode('ASCII')).decode('ASCII')


def decrypt(byt_cipher):
    return base64.b64decode(byt_cipher.encode('ASCII')).decode('ASCII')


if __name__ == "__main__":

    str_plain = "Otter call Melon to rendezvous in Toulouse at 2022-02-04 13:00"
    str_crypt = encrypt(str_plain)
    str_check = decrypt(str_crypt)
    print(f"{str_plain} >> {str_crypt} >> {str_check == str_plain}")
