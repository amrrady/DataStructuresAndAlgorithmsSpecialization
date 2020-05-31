#!/usr/bin/env python3

def calc_fib(n):
    if (n <= 1):
        return n

    prev, curr = 0, 1

    for i in range(2,n + 1):
        prev, curr = curr, (prev + curr)

    return curr

n = int(input())
print(calc_fib(n))
