#!/usr/bin/python3

coins = [1, 2, 5, 10, 20, 50, 100, 200]
calced = {}
def f(n, maxc):
    if n < 0: return 0
    if n == 0: return 1
    if not (n, maxc) in calced: 
        calced[(n, maxc)] =  sum(f(n - c, c) for c in coins if c <= maxc)
    return calced[(n, maxc)]
   
print(f(200, 200))
