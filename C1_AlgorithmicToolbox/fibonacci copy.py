#!/usr/bin/env python3
def calc_fib(n):
    X = 1<<(n+2)
    return pow(X, n+1, X*X-X-1) % X

n = int(input())
print(calc_fib(n))
