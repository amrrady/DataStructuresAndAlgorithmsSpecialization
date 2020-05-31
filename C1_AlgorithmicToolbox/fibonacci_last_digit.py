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


def get_fibonacci_last_digit(n):
    n = n % PisanoPeriod(10)
    if (n <= 1):
        return n

    prev, curr = 0, 1

    for i in range(2,n + 1):
        prev, curr = curr, (prev + curr)

    return curr % 10


num = int(input())
print(get_fibonacci_last_digit(num))
