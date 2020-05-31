#!/usr/bin/env python3

def gcd(a, b):

    tempMin = min(a, b)
    tempMax = max(a, b)

    if tempMin == 0:
        return tempMax

    rem = tempMax % tempMin

    return gcd(rem, tempMin)


a, b = map(int,input().split())
print(gcd(a, b))
