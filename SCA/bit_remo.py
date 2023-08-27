# -*- coding: utf-8 -*-

""" Part of SCA - Simple Crypto Attempts - Not to be considered safe for encryption!
    bit_* is manipulating information on a bit-level,
    e.g. a letter is seen as 8 bits, a 5-letter word is just 40 bits in a row, etc.

    bit_remo holds Reversible Modifiers bit-operations, to be called from other bit_ scripts
"""

import bit_base

def b_seg_flip(lob_in, seg_len=3):
    """ for each segment of a fixed length (seg_len) the order of the bits is flipped
        e.g. seg_flip of 001011 with seg_len = 3 is 100110
        if the total list length is not dividable by seg_len, then the reminder is left untouched (consider rol_flip)
        seg_flip is its own reversible, provided same seg_len in applied
        seg_len = 3 is default as it gives the more printable output - sort of - while not being a factor of 8 """
    # print(f" - init b_seg_flip(<{len(lob_in)}>, {seg_len})")
    num_prts = len(lob_in) // seg_len
    num_main = num_prts * seg_len
    l_main = lob_in[:num_main]
    l_rest = lob_in[num_main:]
    l_ret = list()
    # print(f"lob_in: {lob_in}")
    for n in range(num_prts):
        lst_seg = l_main[n * seg_len : (n + 1) * seg_len]
        # print(f"n: {n}, n+l: {n + seg_len}, [{str(type(lst_seg))}]: {lst_seg}")
        l_ret.extend(reversed(lst_seg))
    l_ret.extend(reversed(l_rest))
    # print(f"lob_ou: {l_ret}")
    return l_ret

def seg_flip(str_in, seg_len):
    """ String accepting wrapper for b_seg_flip """
    lob_in = bit_base.str2lobi(str_in)  # convert to lob
    lob_ou = b_seg_flip(lob_in, seg_len)  # do the modification
    str_ou = bit_base.lobi2str(lob_ou)  # convert back to string
    return str_ou