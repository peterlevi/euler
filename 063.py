#!/usr/bin/python3
print(sum(1 for a in range(1, 10) for b in range(1, 22) if b == len(str(a**b))))
