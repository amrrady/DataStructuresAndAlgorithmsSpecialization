#!/usr/bin/env python3

def selection_sort(A):
    for i in range(0, len(A)):
        minIndex = i
        for j in range(i+1, len(A)):
            if A[j] < A[minIndex]:
                minIndex = j
        
        A[i], A[minIndex] = A[minIndex], A[i]
    return A


data = list(map(int, input().split()))

print(selection_sort(data))