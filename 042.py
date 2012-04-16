#!/usr/bin/python3

def calc(s): return sum(ord(c) - ord('A') + 1 for c in s)
assert calc('SKY') == 55

t = set(i * (i + 1) // 2 for i in range(100))
with open('042_words.txt') as f:
    print(sum(1 for s in f.read().split(',') if calc(s[1:-1]) in t))
