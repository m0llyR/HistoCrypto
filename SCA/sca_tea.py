
# -*- coding: utf-8 -*-

""" Part of SCA - Simple Crypto Attempts - Not to be considered safe for encryption!

    In cryptography, the Tiny Encryption Algorithm (TEA) is a block cipher
    notable for its simplicity of description and implementation,
    typically a few lines of code. It was designed by David Wheeler and
    Roger Needham of the Cambridge Computer Laboratory; it was first presented
    at the Fast Software Encryption workshop in Leuven in 1994,
    and first published in the proceedings of that workshop.

    The cipher is not subject to any patents.

    https://en.wikipedia.org/wiki/Tiny_Encryption_Algorithm """

import os
from pytea import TEA

key = os.urandom(16)
print('key is', key)
content = 'Hello, 你好'
tea = TEA(key)
e = tea.encrypt(content.encode())
print('encrypt hex:', e.hex())
d = tea.decrypt(e)
print('decrypt:', d.decode())