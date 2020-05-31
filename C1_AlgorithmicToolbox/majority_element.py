#!/usr/bin/env python3
import sys

######################### Hash Map ###############################
#### runtime Complexity: O(n)
#### Space Complexity : O(n)

def is_majority_element_HashMap(A):
    count = {}
    for i in range(0, n):
        if A[i] in count : 
            count[A[i]] += 1
            if count[A[i]] > (n//2) : 
                return 1
        else:
            count[A[i]] = 1
    return 0


######################### Divide and Conquer ###############################
#### runtime Complexity: O(n log n)
#### Space Complexity : O(log n)

def is_maj_elem_DivAndConquer(A, l = 0, r =None):
    if(r == l): return A[l]

    mid = (r - l) // 2 + l
    left  = is_maj_elem_DivAndConquer(A, l, mid)
    right = is_maj_elem_DivAndConquer(A, mid+1, r)
    if(left == right):
        return left
    
    left_count  = sum(1 for i in range(l, r + 1) if left  == A[i])
    right_count = sum(1 for i in range(l, r + 1) if right == A[i])

    return left if left_count > right_count else right

def is_majority_element_DivAndConquer(A):
    major = is_maj_elem_DivAndConquer(A, 0, len(A) - 1)

    count = 0
    for i in range(len(A)):
        if A[i] == major:
            count += 1
            if count > (len(A) // 2):
                return 1

    return 0

########################### Boyer-Moore Voting Algorithm ##################
#### runtime Complexity: O( n )
#### Space Complexity : O( 1 )

def is_majority_element_Boyer_Moore_Voting_Algorithm(A):

    count, candidate = 0 , None

    for i in A:
        if count == 0:
            candidate = i
        if i == candidate:
            count += 1
        else:
            count -= 1
    
    count = 0
    for i in A:
        if candidate == i:
            count +=1
            if count > len(A) // 2:
                return 1
    return 0


n = int(input())
A = list(map(int, input().split()))
print(is_majority_element_Boyer_Moore_Voting_Algorithm(A))
