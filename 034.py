#!/usr/bin/python3

f = [1]
for i in range(1, 10):
    f.append(f[-1] * i)

t = 0
for i in range(3, 3000000):
    s = 0
    m = i
    while m > 0:
        s += f[m % 10]
        m //= 10
    if s == i:
        print(i)
        t += s

print('---------')
print(t)

