#!/usr/bin/python3

import itertools

sq = [i*i for i in range(1, 10)]

def ok(A, B):
    AA = set(A)
    if 6 in AA or 9 in AA:
        AA.add(9)
        AA.add(6)
    BB = set(B)
    if 6 in BB or 9 in BB:
        BB.add(9)
        BB.add(6)
    for x in sq:
        a = x // 10
        b = x % 10
        if not(a in AA and b in BB or a in BB and b in AA):
            return False
    return True

assert ok([0, 5, 6, 7, 8, 9], [1, 2, 3, 4, 8, 9])
assert ok([0, 5, 6, 7, 8, 9], [1, 2, 3, 4, 6, 7])

s = 0
for A in itertools.combinations(range(0, 10), 6):
    for B in itertools.combinations(range(0, 10), 6):
        if ok(A, B):
            s += 1
print(s//2) # div by 2, as we are couting each dice pair twice - A,B and B,A
assert s//2 == 1217
