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


def calc_fib(n):
    X = 1<<(n+2)
    return pow(X, n+1, X*X-X-1) % X


def fibonacci_partial_sum(m, n):
    n = n % PisanoPeriod(10)
    m = m % PisanoPeriod(10)
    if (n <= 1):
        return n

    # Sigma Fi -> n = F(n+2) - F(2)
    partial_sum = (calc_fib(n+2) - 1) - (calc_fib(m+1) - 1)
    return partial_sum % 10


m, n = map(int, input().split())
print(fibonacci_partial_sum(m, n))