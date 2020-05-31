#!/usr/bin/env python3

def max_pairwise_product(numbers):
    numbers.sort()
    return numbers[-1] * numbers[-2] 


input_n = int(input())
input_numbers = [int(x) for x in input().split()]
print(max_pairwise_product(input_numbers))
