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


def fibonacci_sum_last_digit( n ):
    n = n % PisanoPeriod(10)
    if (n <= 1):
        return n

    # fib prob sigma Fi^2 = Fn * Fn+1
    return (calc_fib(n) * calc_fib(n+1)) % 10


n = int(input())
print(fibonacci_sum_last_digit(n))
