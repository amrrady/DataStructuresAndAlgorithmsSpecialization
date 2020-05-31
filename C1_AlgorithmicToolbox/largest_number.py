#!/usr/bin/env python3

from functools import cmp_to_key

def numeric_compare(x, y):
    xy = int(str(x) + str(y))
    yx = int(str(y) + str(x))
    return yx - xy


def largest_number(a):
    res = "".join(str(x) for x in sorted(a, key=cmp_to_key(numeric_compare)))
    return res

n = int(input())
data = list(map(int, input().split()))
print(largest_number(data))