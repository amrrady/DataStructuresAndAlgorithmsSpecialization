#!/usr/bin/env python3
import sys

def lcs2(a, b):
    m, n = len(a) + 1, len(b) + 1
    D =  [[0] * m for _ in range(n)] # N x M array of zeros

    for j in range(1, m):
        for i in range(1, n):
            insertion = D[i][j-1]
            deletion  = D[i-1][j]
            mismatch  = D[i-1][j-1]
            match  = D[i-1][j-1] + 1

            if a[j-1] == b[i-1]:
                D[i][j] = max(insertion, deletion, match)
            else:
                D[i][j] = max(insertion, deletion, mismatch)

    return D[n-1][m-1]

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))

    print(lcs2(a, b))
