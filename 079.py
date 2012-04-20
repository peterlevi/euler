#!/usr/bin/python3

m = {}
with open('079_keylog.txt') as f:
    for line in f:
        s = set()
        for c in line.strip():
            m.setdefault(c, set()).update(s)
            s.add(c)
answer = "".join(map(lambda item: item[0], sorted(m.items(), key = lambda tup: len(tup[1]))))
print(answer)
assert answer == '73162890'

