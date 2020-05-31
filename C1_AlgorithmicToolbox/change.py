#!/usr/bin/env python3
import sys

def get_change(m):
    ans = m // 10
    m = m % 10
    ans += m // 5
    m = m % 5
    ans += m

    return ans

m = int(input())
print(get_change(m))
