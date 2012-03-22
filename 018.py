#!/usr/bin/python3

tr = []
with open('018.data', 'r') as f:
    for line in f:
        tr.append(line.split())

for i in range(len(tr) - 2, -1, -1):
    for j in range(len(tr[i])):
        tr[i][j] = int(tr[i][j]) + max(int(tr[i+1][j]), int(tr[i+1][j+1]))

print(tr[0][0])
