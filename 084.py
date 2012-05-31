#!/usr/bin/python3

import random
random.seed()

DICE = 4

M = "GO A1 CC1 A2 T1 R1 B1 CH1 B2 B3 JAIL C1 U1 C2 C3 R2 D1 CC2 D2 D3 FP E1 CH2 E2 E3 R3 F1 F2 U2 F3 G2J G1 G2 CC3 G3 R4 CH3 H1 T2 H2".split()

assert len(M) == 40

def m(s): 
    return M.index(s.upper())

def dice(): 
    return (random.randint(1, DICE), random.randint(1, DICE))

def isCc(pos):
    return M[pos][:2] == "CC"

def isCh(pos):
    return M[pos][:2] == "CH"

def findNext(pos, c):
    i = pos
    while True:
        i = (i + 1) % len(M)
        if M[i][0] == c and len(M[i]) == 2:
            break
    return i

assert findNext(0, 'R') == 5
assert findNext(0, 'C') == 11
assert findNext(38, 'U') == 12

statCc = ["GO", "JAIL"]
statCh = ["GO", "JAIL", "C1", "E3", "H2", "R1"]

cc = []
cci = 0
ch = []
chi = 0

def process(pos):
    global cc
    global ch
    global cci
    global chi
    if isCc(pos):
#        print(M[pos], cc[0], cc)
        x = cc[cci]
        cci = (cci + 1) % 16
        if x < len(statCc):
            return (m(statCc[x]), True)
        return (pos, False)
    elif isCh(pos):
#        print(M[pos], ch[0], ch)
        x = ch[chi]
        chi = (chi + 1) % 16
        if x < len(statCh):
            return (m(statCh[x]), True)
        elif x == 6 or x == 7:
            return (findNext(pos, 'R'), True)
        elif x == 8:
            return (findNext(pos, 'U'), True)
        elif x == 9:
            return ((pos - 3) % len(M), True)
        else:
            return (pos, False)


visits = [0] * len(M)

def game(C):
    global cc
    global ch
    global cci
    global chi
    random.seed()

    cc = list(range(16))
    cci = 0
    random.shuffle(cc)
    ch = list(range(16))
    chi = 0
    random.shuffle(ch)

    pos = 0
    doubles = 0

    for i in range(C):
        d = dice()
#        print(M[pos], d)
        if d[0] == d[1]:
            doubles += 1
            if doubles == 3:
                doubles = 0
                pos = m("JAIL")
                visits[pos] += 1
                continue
        else:
            doubles = 0
        pos = (pos + d[0] + d[1]) % len(M)
        if pos == m("G2J"):
            pos = m("JAIL")
        while isCc(pos) or isCh(pos):
            (pos, moved) = process(pos)
            if not moved:
                break
#        print("end in ", M[pos])
        visits[pos] += 1

for i in range(100):
    game(50000)

s = sum(visits)
percents = [x*100/s for x in visits]
print(sorted([(v, i, M[i]) for i, v in enumerate(percents)], reverse=True)[:6])

