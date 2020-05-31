#!/usr/bin/env python3

def optimal_summands(n):
    if n < 3: return [n]

    summands = []
    x = 1
    while(n > 0):
        if x <= n :
            summands.append(x)
            n -= x
            x += 1 
        else :
            summands[-1] += n
            break

    return summands


n = int(input())
summands = optimal_summands(n)
print(len(summands))
print(' '.join(str(x) for x in summands))
