# -*- coding: utf-8 -*-

""" Part of SCA - Simple Crypto Attempts - Not to be considered safe for encryption!
    bit_* is manipulating information on a bit-level,
    e.g. a letter is seen as 8 bits, a 5-letter word is just 40 bits in a row, etc.

    bit_base holds basic bit-operations, to be called from other bit_ scripts
"""

import base64
# import bitarray  # see: https://github.com/ilanschnell/bitarray

# dic_b64 = {  We do not do b64 any more...
#     0: 'A',
#     1: 'B',
#     2: 'C',
#     3: 'D',
#     4: 'E',
#     5: 'F',
#     6: 'G',
#     7: 'H',
#     8: 'I',
#     9: 'J',
#     10: 'K',
#     11: 'L',
#     12: 'M',
#     13: 'N',
#     14: 'O',
#     15: 'P',
#     16: 'Q',
#     17: 'R',
#     18: 'S',
#     19: 'T',
#     20: 'U',
#     21: 'V',
#     22: 'W',
#     23: 'X',
#     24: 'Y',
#     25: 'Z',
#     26: 'a',
#     27: 'b',
#     28: 'c',
#     29: 'd',
#     30: 'e',
#     31: 'f',
#     32: 'g',
#     33: 'h',
#     34: 'i',
#     35: 'j',
#     36: 'k',
#     37: 'l',
#     38: 'm',
#     39: 'n',
#     40: 'o',
#     41: 'p',
#     42: 'q',
#     43: 'r',
#     44: 's',
#     45: 't',
#     46: 'u',
#     47: 'v',
#     48: 'w',
#     49: 'x',
#     50: 'y',
#     51: 'z',
#     52: '0',
#     53: '1',
#     54: '2',
#     55: '3',
#     56: '4',
#     57: '5',
#     58: '6',
#     59: '7',
#     60: '8',
#     61: '9',
#     62: '+',
#     63: '/'
# }


def str2lobi(str_in):
    """ string to bitlist (lobi: list of bits)
        Steal from https://stackoverflow.com/questions/10237926/convert-string-to-list-of-bits-and-viceversa
        org. name: s_to_bitlist(s) """
    # ToDo[] This, or it's reverse, do not seem to work with higher Unicode numbers like ☰☱☲☳☴☵☶☷
    ords = (ord(c) for c in str_in)
    shifts = (7, 6, 5, 4, 3, 2, 1, 0)
    return [(o >> shift) & 1 for o in ords for shift in shifts]

def lobi2loc(lobi_in):
    """ Helperfunction for "bitlist to string"
        lobi: list of bits
        loc: list of chars
        Steal from https://stackoverflow.com/questions/10237926/convert-string-to-list-of-bits-and-viceversa
        org. name: bitlist_to_chars(bl) """
    # ToDo[] This, or it's reverse, do not seem to work with higher Unicode numbers like ☰☱☲☳☴☵☶☷
    bi = iter(lobi_in)
    bytes = zip(*(bi,) * 8)
    shifts = (7, 6, 5, 4, 3, 2, 1, 0)
    for byte in bytes:
        yield chr(sum(bit << s for bit, s in zip(byte, shifts)))

def lobi2str(lobi_in):
    """ bitlist (lobi: list of bits) to string
        Steal from https://stackoverflow.com/questions/10237926/convert-string-to-list-of-bits-and-viceversa
        org. name: bitlist_to_s(bl) """
    str_ret = ''.join(lobi2loc(lobi_in))
    # print(f":: lobi2str({lobi_in}) = {str_ret}")
    return str_ret


def sixbit2b64(lob_in):
    """ """
    num_ou = 0
    for bit in lob_in:
        num_ou = (num_ou << 1) | bit
    return dic_b64[num_ou]


def labi2copra(lob_in):
    """ Convert the lobi (list of bits) to copra (Compact Printable Ascii)
        This is NOT base64 encoding, but will likevise create a printable string of selected 7-bit ascii
        Details T.B.D."""
    return "Not implemented yet..."

# def lobi2b64(lob_in):
#     """ convert the lobi (list of bits) to a base64 ascii string
#         base64.b64encode() won't do is as it fails on non-ascii input """
#     FORGET IT - b64 requires byte (8-bit) input, and processes in 24-bit groups - we can't meet that requirement!
#     #ToDo[44] TEST this
#     #ToDo[11] Write the reverse function
#     seg_len = 6  # 6-bit gives length 64 alphabet.
#     num_prts = len(lob_in) // seg_len
#     num_main = num_prts * seg_len
#     l_main = lob_in[:num_main]
#     l_rest = lob_in[num_main:]
#     str_ret = str()
#     for n in range(num_prts):
#         lst_seg = l_main[n * seg_len : (n + 1) * seg_len]
#         str_ret += sixbit2b64(lst_seg)
#     str_rest = lobi2str(l_rest)  #ToDo[50] DEAL with the rest in an official bqse64 way !!!
#     print(f"::lobi2b64():: str_rest: {str_rest}")
#     str_ret += str_rest
#     return str_ret


if __name__ == '__main__':

    # Just 4 fun

    str_sim = "This is 1 #%& bloody simple text string!"  # missing ¤ ÆØÅæøå
    str_adv = "This is advanced with Ꮺ Ψ ☰☱☲☳☴☵☶☷ ° and many more..."
    print(f"{str_sim}\n{str_adv}")

    byt_sim = str_sim.encode(encoding='utf-8', errors='strict')
    byt_adv = str_adv.encode(encoding='utf-8', errors='strict')
    # print(f"byt.: {byt_sim}")
    # print(f"byt.: {byt_adv}")

    bya_sim = bytearray(str_sim, encoding='utf-8', errors='strict')
    bya_adv = bytearray(str_adv, encoding='utf-8', errors='strict')
    # print(f"bya.: {bya_sim}")
    # print(f"bya.: {bya_adv}")

    str_resim = byt_sim.decode(encoding='utf-8', errors='strict')
    str_readv = bya_adv.decode(encoding='utf-8', errors='strict')

    print("Return to origin...")
    print(f"Re-sim: {str_resim == str_sim}")  # \n\t{str_sim}\n\t{str_resim}")
    print(f"Re-adv: {str_readv == str_adv}")

    # print("\n * Exploring 3'rd party bitarray module")
    # bia_sim = bitarray.bitarray()
    # bia_sim.frombytes(str_sim.encode('utf-8'))
    # print(f"bia_sim: {bia_sim}")
    # str_unbia_sim = bitarray.bitarray(bia_sim).tobytes().decode('utf-8')
    # print(f"Re-sim: {str_unbia_sim == str_sim}")

    print("\n * Test steal from https://stackoverflow.com/questions/10237926/convert-string-to-list-of-bits-and-viceversa")
    str_in = str_sim
    nbl_in = str2lobi(str_in)  # native bit-list
    str_renbl_hi = lobi2str(nbl_in)
    print(f"NBL (len:{len(nbl_in)}) : {nbl_in}\nRe-nbl: {str_renbl_hi == str_in}")

    # print(f"NBL as b64: {lobi2b64(nbl_in)}")

