#!/usr/bin/python3

m = {}
i = 0
candidates = []
while True:
    i += 1
    cube = i**3
    base = "".join(sorted(str(cube)))
    m.setdefault(base, []).append(str(cube))
    if len(m[base]) == 5:
        candidates.append(m[base])
    elif len(m[base]) == 6:
        candidates.remove(m[base])
    if len(candidates) > 0 and len(base) > len(candidates[0][0]) and len([c for c in candidates if len(c) == 5]) > 0:
        break
print(candidates)
print("----")
print(min(c[0] for c in candidates))
