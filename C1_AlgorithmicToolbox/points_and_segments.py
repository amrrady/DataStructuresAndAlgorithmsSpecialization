#!/usr/bin/env python3

def fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    #write your code here
    return cnt

def is_in_range(ranges, point):

    if len(ranges) and (point < ranges[0][0] or point > ranges[0][1]):
        return 0

    within_ranges = 0
    for i in range(len(ranges)):
        if ranges[i][0] <= point and point <= ranges[i][1]:
            within_ranges += 1
        elif ranges[i][0] > point:
            break

    return within_ranges

def naive_count_segments(ranges, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        cnt[i] += is_in_range(ranges, points[i])

    return cnt

n, m = map(int,input().split())

ranges = []
for i in range(0, n):
    l, r = map(int,input().split())
    ranges.append((l,r))

ranges = sorted(ranges, key=lambda tup: tup[0])
print(ranges)
points = list(map(int,input().split()))

print(*naive_count_segments(ranges, points))