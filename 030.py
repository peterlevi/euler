#!/usr/bin/python3

def sumDigits(i):
    if i < 10: return i**5
    return (i % 10)**5 + sumDigits(i // 10)

assert sumDigits(23) == 275
print(sum(i for i in range(2, 360000) if i == sumDigits(i)))
