#!/usr/bin/python
from gmpy import mpz

counts = {}

def solve():
    p = 2
    while True:
        p = int(mpz(p).next_prime())
        s = str(p)
        for a in range(len(s) - 2):
            for b in range(a + 1, len(s) - 1):
                for c in range(b + 1, len(s)):
                    if s[a]==s[b]==s[c]:
                        s1 = s[:a] + '*' + s[a+1:b] + '*' + s[b+1:c] + '*' + s[c+1:]
                        if s1 == '*2*3*3': print(s)
                        counts[s1] = counts.setdefault(s1, 0) + 1
                        if counts[s1] == 8:
                            print('sol: ' + s1)
                            return

solve()
