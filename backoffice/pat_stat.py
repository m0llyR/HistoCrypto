#!/usr/bin/python
# -*- coding: utf-8 -*-

""" pattern stat """

fn = r"data/patters.txt"

with open(fn, encoding="utf-8") as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]
cont = "".join(content)
print(f"cont: {content}")
print(f"cont: {cont}")

num_min_seq = 3
num_max_seq = 12

dic_sequ = dict()
for num_seqlen in range(num_min_seq, num_max_seq + 1):
    print(f"Sequence: {num_seqlen}")
    dic_sequ[num_seqlen] = dict()
    for n in range(len(cont) - num_seqlen):
        sequ = cont[n:n+num_seqlen]
        # print(f".sequ: {sequ}")
        if sequ not in dic_sequ[num_seqlen].keys():
            dic_sequ[num_seqlen][sequ] = 1
        else:
            dic_sequ[num_seqlen][sequ] += 1

for ka in dic_sequ.keys():
    print(f"Sequence length: {ka}")
    for kb in sorted(dic_sequ[ka].keys()):
        if dic_sequ[ka][kb] > 1:
            print(f"  seq: {kb}: {dic_sequ[ka][kb]}")
