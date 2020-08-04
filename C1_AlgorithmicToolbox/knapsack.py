#!/usr/bin/env python3
import sys

def optimal_weight(W, weights):
    weights.insert(0,0)
    results =  [[0] * (W + 1) for _ in range(len(weights))] # N x M array of zeros

    for i in range(1, len(weights)):
        for w in range(1, W + 1):
            results[i][w] = results[i-1][w]
            if weights[i] <= w:
                val = results[i-1][w - weights[i]] + weights[i]
                if val > results[i][w]:
                    results[i][w] = val

    return results[len(weights) -1][W]

def main():
    W, _ = map(int, input().split())
    w = list(map(int, input().split()))

    print(optimal_weight(W, w))

if __name__ == '__main__':
    main()

