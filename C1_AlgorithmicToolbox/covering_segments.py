#!/usr/bin/env python3

from functools import cmp_to_key


def comp(x1):
    return x1[1]


def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))


def optimal_points(segments):
    answer = []
    while len(segments) > 0:
        right = segments[0][1]
        if right not in answer:
            answer.append(right)
        segments = [x for x in segments if right not in range(x[0] , x[1]+1)]

    return answer


n = int(input())
data = []
for i in range(n):
    x, y = input().split()
    data.append((int(x), int(y)))
data = sorted(data, key=comp)
points = optimal_points(data)
print(len(points))
print(*points)
