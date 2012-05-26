#!/usr/bin/python3

import math

m = 0
mi = 0
with open('099_base_exp.txt') as f:
    for i, l in enumerate(f):
        (a, b) = map(int, l.split(','))
        x = b * math.log(a)
        if x > m:
            m = x
            mi = i
print(mi + 1)

