#!/usr/bin/python3

print(sum((i + 1)* sum((ord(c) - ord('A') + 1) for c in x[1:-1]) for i, x in enumerate(sorted(open('022_names.txt').read().split(',')))))
