#!/usr/bin/python3

with open('013.data', 'r') as f:
    sum = 0
    for line in f: 
        if line.strip():
            sum += int(line.strip())

    print(str(sum)[:10])

