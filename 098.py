#!/usr/bin/python3

from math import sqrt

def describe(a, b):
    result = []
    for x in a:
        result.append(b.index(x))
    return tuple(result)

s = ""
with open('098_words.txt') as f:
    s = f.read()

a = {}
descriptions = {}
for w in s.split(','):
    w = w[1:-1]
    a.setdefault(tuple(sorted(w)), []).append(w)
for v in a.values():
    for w1 in v:
        for w2 in v:
            if w1 != w2:
                descriptions[describe(w1, w2)] = (w1, w2)

b = {}
for i in range(int(sqrt(10)), int(sqrt(10**9)) + 2):
    i2 = str(i*i)
    if len(set(i2)) == len(i2):
        b.setdefault(tuple(sorted(i2)), []).append(i*i)

for v in b.values():
    for a in v:
        for b in v:
            if a != b and describe(str(a), str(b)) in descriptions:
                print(a, b, descriptions.get(describe(str(a), str(b))))


