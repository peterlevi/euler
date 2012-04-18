#!/usr/bin/python3

import math

n = 0
while True:
    n += 1
    x = n*(3*n - 1) // 2
    h = (math.sqrt(8*x + 1) + 1) / 4
    t = (math.sqrt(8*x + 1) - 1) / 2
    if int(h) == h and int(t) == t and x > 40755:
        print(x)
        break

