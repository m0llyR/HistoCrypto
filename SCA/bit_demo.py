# -*- coding: utf-8 -*-

""" Part of SCA - Simple Crypto Attempts - Not to be considered safe for encryption!
    bit_* is manipulating information on a bit-level,
    e.g. a letter is seen as 8 bits, a 5-letter word is just 40 bits in a row, etc.

    bit_demo is a demonstration of how to use bit_* encryption
"""

import bit_remo

str_sim = "This is 1 #¤%& bloody simple ÆæØøÅå text string!"
print(f"{str_sim}")

str_case = str_sim  # Simple Segment Flip is not safe for higher Unicode numbers !!!
num_maxf = 8
print(f"\nSimple Segment Flip (length {num_maxf})")
print(f"inp: {str_case}")
for slen in range(2, num_maxf):
    str_in_sf3 = bit_remo.seg_flip(str_case, slen)
    print(f"sf{slen}: {str_in_sf3}")
    str_un_sf3 = bit_remo.seg_flip(str_in_sf3, slen)
    print(f"ret: {str_un_sf3} << Returned correct: {str_un_sf3 == str_case}")
