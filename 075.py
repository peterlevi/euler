#!/usr/bin/python3

import math

MAX = 1500001 

aa = [0] * MAX
bb = [0] * MAX
cc = [0] * MAX

for m in range(1, int(math.sqrt(MAX))):
    for n in range(1, m):
        for k in range(1, MAX // (m**2 + n**2)):
            a = k * (m**2 - n**2)
            b = k * 2 * m * n
            c = k * (m**2 + n**2)
            L = a + b + c
            if L < MAX:
                if aa[L] == 0:
                    aa[L] = a
                    bb[L] = b
                    cc[L] = c
                elif sorted([a, b, c]) != sorted([aa[L], bb[L], cc[L]]):
                    aa[L] = bb[L] = cc[L] = -1


print(sum(1 for a in aa if a > 0))
