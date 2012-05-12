#!/usr/bin/python3

facts = [1]
for i in range(1, 10):
    facts.append(facts[-1] * i)

def calc(n):
    s = 0
    while n > 0:
        s += facts[n % 10]
        n //= 10
    return s

assert calc(169) == 363601
assert calc(363601) == 1454

def cycle(n):
    l = 0
    seen = set()
    while not n in seen:
        l += 1
        seen.add(n)
        n = calc(n)
    return l

assert cycle(145) == 1
assert cycle(169) == 3
assert cycle(69) == 5

print(sum(1 for n in range(1, 10**6) if cycle(n) == 60))
