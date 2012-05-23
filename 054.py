#!/usr/bin/python3

R = {'T' : 10, 'J' : 11, 'Q' : 12, 'K' : 13, 'A' : 14}
for i in range(2, 10):
    R[chr(ord('0') + i)] = i

SR = { i : 2**i for i in range(1, 15) }
SC = {1 : 1, 2 : 10**10, 3 : 10**20, 4 : 10**40}

ORDER = [([], False, False), ([2], False, False), ([2, 2], False, False), ([3], False, False), ([], True, False), ([], False, True), ([3, 2], False, False), ([4], False, False), ([], True, True)]

def score(hand):
    byRank = {}
    byColor = {}
    ranks = []

    for c in hand:
        ranks.append(R[c[0]])
        byRank.setdefault(c[0], []).append(c)
        byColor.setdefault(c[1], []).append(c)

    ranks = sorted(ranks)

    counts = sorted([c for c in map(len, byRank.values()) if c > 1], reverse = True)

    straight = len(counts) == 0 and ranks[-1] - ranks[0] == 4

    flush = len(byColor) == 1

    order = ORDER.index((counts, straight, flush))

    score = order * (10**60)
    for k, l in byRank.items():
        score += SC[len(l)] * SR[R[k]]

    return score


testHands = [
    "8H 9C 6S JS QD", 
    "3H 4C 5S 6S KD", 
    "9H 9C 6S JS QD", 
    "9H 9C 6S 7S KD",
    "JH JS 2C 3C 4C",
    "8H 8C 9H 9C 2C",
    "8H 8C 9H 9C 3C",
    "JH JC 2H 2C 3C",
    "3H 3C 3S 7S QD",
    "3H 3C 3S 2S KD",
    "4H 4C 4S 2S QD",
    "2H 3C 4S 5S 6D",
    "3C 4S 5S 6D 7D",
    "2H 4H 5H 7H 8H",
    "2H 3H 5H 6H 9H",
    "5H 5C 5S 2S 2D",
    "5H 5C 5S KS KD",
    "6H 6C 6S 2S 2D",
    "2H 2C 2S 2S 3D",
    "2H 2C 2S 2S KD",
    "3H 3C 3S 3S 2D",
    "2H 3H 4H 5H 6H",
    "3H 4H 5H 6H 7H"
]

sc = 0
for h in testHands:
    newsc = score(h.split())
    assert newsc > sc
    sc = newsc

cnt = 0
with open('054_poker.txt') as f:
    for l in f:
        a = l.split()
        win = score(a[:5]) > score(a[5:])
        if win:
            cnt += 1

print(cnt)
assert cnt == 376
