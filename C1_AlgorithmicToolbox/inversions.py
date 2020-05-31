#!/usr/bin/env python3
import sys


def merge_and_count(A, left, mid, right):
    inversions = 0
    leftArr = A[left:mid + 1]
    rightArr = A[mid + 1:right + 1]

    i, j, k = 0, 0, left
    while i < len(leftArr) and j < len(rightArr):
        if leftArr[i] <= rightArr[j]:
            A[k] = leftArr[i]
            i += 1
        else:
            A[k] = rightArr[j]
            j += 1
            inversions += len(leftArr) - i
        k += 1

    while i < len(leftArr):
        A[k] = leftArr[i]
        k += 1
        i += 1

    while j < len(rightArr):
        A[k] = rightArr[j]
        k += 1
        j += 1

    return inversions


def sub_array_inversions(A, left, right):
    if left >= right: return 0

    mid = left + ((right - left) // 2)

    return (sub_array_inversions(A, left, mid)
            + sub_array_inversions(A, mid + 1, right)
            + merge_and_count(A, left, mid, right))


def get_number_of_inversions(A):
    return sub_array_inversions(A, 0, len(A) - 1)


n = int(input())
A = list(map(int, input().split()))
print(get_number_of_inversions(A))
