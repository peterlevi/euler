#!/usr/bin/python3
p = set(n*(3*n - 1) // 2 for n in range(1, 10000))
for x in p:
    for y in p:
        if x != y and x - y in p and x + y in p:
            print(x - y)
# proof that this is the minimum?
