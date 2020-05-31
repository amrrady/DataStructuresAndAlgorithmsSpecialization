#!/usr/bin/env python3

def compute_min_refills(distance, tank, stops):
    stops.insert(0,0)
    stops.append(distance)
    index = 1
    refills = 0
    startingPos = stops[0]
    while index  < len(stops):
        if stops[index] > startingPos + tank :
            return -1
        elif index + 1 < len(stops) and stops[index + 1] > startingPos + tank :
            refills += 1
            startingPos = stops[index]

        index += 1

    return refills

d = int(input())
t = int(input())
n = int(input())

stops = [int(x) for x in input().split()]
print(compute_min_refills(d, t, stops))
