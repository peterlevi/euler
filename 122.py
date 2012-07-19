#!/usr/bin/python

def parents(t):
    yield t
    while m[t][1] is not None:
        t = m[t][1]
        yield t

solved = set([1])
s = 0

cnt = 0
m = {}
m[cnt] = (1, None)
leafs = [cnt]

while True:
    newleafs = []
    for c in leafs:
        for p in parents(c):
            val = m[c][0] + m[p][0]
            if val > 200:
                continue
            if not val in solved:
                s += len(list(parents(c)))
                solved.add(val)
                if len(solved) == 200:
                    print s
                    exit()
            cnt += 1
            m[cnt] = (val, c)
            newleafs.append(cnt)
    leafs = newleafs

