#!/usr/bin/python3
a = [x for x in range(0, 21)]
p = 1
for x in range(2, 21):
    p *= a[x]
    for i in range(x + x, 21, x):
        a[i] /= a[x]

print(p)
