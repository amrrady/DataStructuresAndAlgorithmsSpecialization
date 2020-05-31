#!/usr/bin/env python3

from random import randint

def partition_3(A, l, r):
    x, i, j, k = A[l], l, l, r

    while i <= k:
        if A[i] < x:
            A[i], A[j] = A[j], A[i]
            j += 1
        elif A[i] > x:
            A[i], A[k] = A[k], A[i]
            k -= 1
            i -= 1
        i += 1

    return j, k

def randomized_quick_sort(A, l, r):
    if l >= r: return

    pivot = randint(l,r)
    A[pivot], A[l] = A[l], A[pivot]

    m1, m2 = partition_3(A, l, r)

    randomized_quick_sort(A, l, m1-1)
    randomized_quick_sort(A, m2+1, r)
    return

def randomized_quick_sort_wrapper(A):
    randomized_quick_sort(A, 0, len(A) - 1)
    return A


n = int(input())
A = list(map(int, input().split()))
print(" ".join(str(i) for i in randomized_quick_sort_wrapper(A)))
