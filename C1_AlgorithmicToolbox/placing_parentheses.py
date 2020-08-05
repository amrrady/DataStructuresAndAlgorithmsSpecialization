#!/usr/bin/env python3

import math
import re


def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def MinAndMax(i, j, Op, Min, Max):
    maxVal = - math.inf
    minVal = math.inf
    for k in range(i, j):
        a = evalt(Max[i][k], Max[k+1][j], Op[k])
        b = evalt(Max[i][k], Min[k+1][j], Op[k])
        c = evalt(Min[i][k], Max[k+1][j], Op[k])
        d = evalt(Min[i][k], Min[k+1][j], Op[k])

        minVal = min(minVal, a, b, c, d)
        maxVal = max(maxVal, a, b, c, d)

    return (minVal, maxVal)




def get_maximum_value(dataset):
    Numbers = list(map(int,re.split("[+-/*]", dataset)))
    Ops = re.findall("[+-/*]", dataset)

    n = len(Numbers)

    Min = [[0] * n for _ in range(n)]
    Max = [[0] * n for _ in range(n)]

    for i in range(n):
        Min[i][i] = Numbers[i]
        Max[i][i] = Numbers[i]

    for s in range(1, n):
        for i in range(n-s):
            j = i + s
            Min[i][j], Max[i][j] = MinAndMax(i, j, Ops, Min, Max)

    return Max[0][n-1]


if __name__ == "__main__":
    print(get_maximum_value(input()))
