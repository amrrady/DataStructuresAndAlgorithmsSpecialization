#!/usr/bin/env python3

# LIMITED TO 32 ELEMENTS
def get_key(elem):
    return elem

def count_sort(A):
    count = [[] for i in range(32)] # array of k empty lists

    for i in range(0, len(A)):
        count[get_key(A[i])].append(A[i])

    print("count")
    print(count)

    output = []

    for i in range(0, 32):
        output.extend(count[i])  # O(n + k)

    return output


data = list(map(int, input().split()))
ans = count_sort(data) 
print(ans)