#!/usr/bin/env python3
import sys

def binary_srch(A,l,r, x):
    if l > r : return -1

    mid = int((r + l) // 2)
    if A[mid] == x :
        return mid
    
    if A[mid] > x:
        return binary_srch(A, l,  mid - 1, x)
    
    if A[mid] < x:
        return binary_srch(A, mid + 1, r, x)

    return -1

def binary_search(A, x):
    l = 0
    r = len(A) - 1
    return binary_srch(A, l, r, x)




data = list(map(int, input().split()))[1:]
elements = list(map(int, input().split()))[1:]

print(" ".join([ str(binary_search(data, i)) for i in elements]))