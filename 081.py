#!/usr/bin/python3

m = []
with open('081_matrix.txt') as f:
    for l in f:
        m.append(l.split(','))

best = list(m)
for i, line in enumerate(m):
    for j, a in enumerate(line):
        mm = 10**9
        if i > 0: mm = best[i-1][j]
        if j > 0 and best[i][j-1] < mm: mm = best[i][j-1]
        if mm == 10**9: mm = 0
        best[i][j] = int(m[i][j]) + mm
print(best[-1][-1])
