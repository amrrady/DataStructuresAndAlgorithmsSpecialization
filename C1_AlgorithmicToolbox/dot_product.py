#!/usr/bin/env python3

def max_dot_product(a, b):
    a.sort(reverse = True)
    b.sort(reverse = True)
    res = 0
    for i in range(len(a)):
        res += a[i] * b[i]
    return res

n = int(input())
a =  [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
print(max_dot_product(a, b))
