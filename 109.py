#!/usr/bin/python3

doubles = [2*x for x in range(1, 21)] + [50]
allp = sorted([x for x in range(1, 21)] + [25] + doubles + [3*x for x in range(1, 21)])

def c(n):
    cnt = 0
    for d in doubles:
        if d > n:
            break
        if d == n:
            cnt += 1
            break
        r = n - d
        for i in range(0, len(allp)):
            if allp[i] == r:
                cnt += 1
            if allp[i] > r:
                break
            for j in range(i, len(allp)):
                if allp[i] + allp[j] == r:
                    cnt += 1
                if allp[i] + allp[j] > r:
                    break
        
    return cnt

print(sum(c(i) for i in range(1, 100)))
