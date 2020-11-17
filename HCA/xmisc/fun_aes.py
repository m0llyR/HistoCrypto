import sys
import base64
from Crypto.Cipher import AES


class AESCipher(object):
    def __init__(self, key):
        self.bs = 16
        self.cipher = AES.new(key, AES.MODE_ECB)

    def encrypt(self, raw):
        raw = self._pad(raw)
        encrypted = self.cipher.encrypt(raw)
        encoded = base64.b64encode(encrypted)
        return str(encoded, 'utf-8')

    def decrypt(self, raw):
        decoded = base64.b64decode(raw)
        decrypted = self.cipher.decrypt(decoded)
        return str(self._unpad(decrypted), 'utf-8')

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    def _unpad(self, s):
        return s[:-ord(s[len(s)-1:])]


if __name__ == '__main__':
    key = 'kfu7q4ujyr1p8nwmgo5d9ldb7f5p7jrq'
    cipher = AESCipher(key)

    plaintext = '542#1504891440039'
    plaintext = "If you read this, then I'm sorry to say that this algorithm can no longer be considered safe for serious use ..."
    encrypted = cipher.encrypt(plaintext)
    print('Encrypted: %s' % encrypted)
    ciphertext = 'L2+kZD0aWIQNZ4CXxLYbe22/d1ZT5vNE3oZM73xPIMAJsuUV+rF9JVU1z0lEv8UlgaO80x8amAtRQ8YqoNyjbh+/NwJefai3yr/bTjr2QOAnOchN314gcylWDbexgEYoW1PX4PkzH/OotQXIL1JF48L5lf0n38d0bK4KGjTCNyQ='
    assert encrypted == ciphertext

    decrypted = cipher.decrypt(encrypted)
    print('Decrypted: %s' % decrypted)
    assert decrypted == plaintext

"""
L2+kZD0aWIQNZ4CXxLYbe22/d1ZT5vNE
3oZM73xPIMAJsuUV+rF9JVU1z0lEv8Ul
gaO80x8amAtRQ8YqoNyjbh+/NwJefai3
yr/bTjr2QOAnOchN314gcylWDbexgEYo
W1PX4PkzH/OotQXIL1JF48L5lf0n38d0
bK4KGjTCNyQ=
"""