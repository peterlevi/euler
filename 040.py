#!/usr/bin/python3

i = 1
count = 1
digs = 1
nextDigs = 10
p = 1
for d in range(7):
    while count < 10**d:
        i += 1
        if i >= nextDigs:
            digs += 1
            nextDigs *= 10
        count += digs

    p *= int(str(i)[-(count - 10**d) - 1])

print(p)
