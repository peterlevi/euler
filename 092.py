#!/usr/bin/python3

def sumdsq(j):
    s = 0
    while j > 0:
        s += (j % 10) * (j % 10)
        j //= 10
    return s 

m = [0] * (7*9*9 + 1)
m[1] = 1
m[89] = 89
for i in range(1, 7*9*9 + 1):
    seq = []
    j = i
    while True:
        if m[j] > 0:
            for x in seq:
                m[x] = m[j]
            break
        seq.append(j)
        j = sumdsq(j)
assert m[44] == 1
assert m[85] == m[145] == 89

s = 0
for i in range(1, 10**7):
    if m[sumdsq(i)] == 89:
        s += 1
print(s)

assert s == 8581146

