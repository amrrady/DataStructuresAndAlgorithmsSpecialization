#!/usr/bin/env python3

import sys

def edit_distance(a, b):
    m, n = len(a) + 1, len(b) + 1
    D =  [[sys.maxsize] * m for _ in range(n)] # N x M array of zeros
    for i in range(m):
        D[0][i] = i
    for i in range(n):
        D[i][0] = i

    for j in range(1, m):
        for i in range(1, n):
            insertion = D[i][j-1] + 1
            deletion  = D[i-1][j] + 1
            mismatch  = D[i-1][j-1] + 1
            match  = D[i-1][j-1]

            if a[j-1] == b[i-1]:
                D[i][j] = min(insertion, deletion, match)
            else:
                D[i][j] = min(insertion, deletion, mismatch)

    return D[n-1][m-1]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
