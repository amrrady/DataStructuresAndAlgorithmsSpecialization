#!/usr/bin/env python3
import sys

def optimal_sequence(n):
    sequence = {0:0, 1:0, 2:1, 3:1}
    ops = {0:"0", 1:"1", 2:"1 2", 3:"1 3"}
    for i in range(4, n+1):
        sequence[i] = sys.maxsize

        if i % 3 == 0 and sequence[i/3] + 1 < sequence[i]:
            sequence[i] = sequence[i/3] + 1
            ops[i] = "{} {}".format(ops[i / 3], i)

        if i % 2 == 0 and sequence[i/2] + 1 < sequence[i]:
            sequence[i] = sequence[i/2] + 1
            ops[i] = "{} {}".format(ops[i / 2], i)

        if sequence[i-1] + 1 < sequence[i]:
            sequence[i] = sequence[i-1] + 1
            ops[i] = "{} {}".format(ops[i - 1], i)


    return (sequence[n],ops[n])


def main():
    n = int(input())
    results = optimal_sequence(n)
    print(results[0])
    print(results[1])

if __name__ == "__main__":
    main()
