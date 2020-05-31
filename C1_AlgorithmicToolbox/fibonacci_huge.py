#!/usr/bin/env python3

def PisanoPeriod(m):

    if m == 1:
        return m
    prev, curr = 0, 1

    for i in range(0, m * m):
        prev, curr = curr, (prev + curr) % m
        if prev == 0 and curr == 1:
            return i+1
    return 1


def get_fibonacci_mod(n, m):
    n = n % PisanoPeriod(m)
    if (n <= 1):
        return n

    prev, curr = 0, 1

    for i in range(2,n + 1):
        prev, curr = curr, (prev + curr)

    return curr % m

n, m = map(int,input().split())
print(get_fibonacci_mod(n, m))
