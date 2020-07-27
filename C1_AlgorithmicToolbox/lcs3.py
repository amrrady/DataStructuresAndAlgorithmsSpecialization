#!/usr/bin/env python3
import sys

def dim(a):
    if not type(a) == list:
        return []
    return [len(a)] + dim(a[0])

def lcs3(a, b, c):
    x, y, z = len(a), len(b), len(c)
    D =  [[[0 for i in range(z+1)] for j in range(y+1)] for k in range(x+1)] 

    for i in range(1, x+1):
        for j in range(1, y+1):
            for k in range(1, z+1):
                if (a[i-1] == b[j-1] and a[i-1] == c[k-1]): 
                    D[i][j][k] = D[i-1][j-1][k-1] + 1
                else:
                    D[i][j][k] = max(D[i-1][j][k], D[i][j-1][k], D[i][j][k-1])


    return D[x][y][z]

if __name__ == '__main__':
    _ = int(input())
    a = list(map(int, input().split()))
    _ = int(input())
    b = list(map(int, input().split()))
    _ = int(input())
    c = list(map(int, input().split()))
    print(lcs3(a, b, c))
