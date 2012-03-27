#!/usr/bin/python3

a = b = 1
t = 10**(1000-1)
i = 1
while a < t:
    i += 1
    b = a + b
    a = b - a
print(i)
