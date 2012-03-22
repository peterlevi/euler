#!/usr/bin/python

print([(a, b, 1000-a-b, a*b*(1000-a-b)) for a in range(1, 1000) for b in range(a, 1000) if a**2 + b**2 == (1000 - a - b)**2])
