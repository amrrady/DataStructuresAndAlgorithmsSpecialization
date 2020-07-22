#!/usr/bin/env python3

import sys

def get_change(money, coins):
    numCoins = {0:0}
    for m in range(1, money + 1):
        numCoins[ m ] = sys.maxsize
        for coin in coins:
            if m >= coin:
                num = numCoins[m - coin] + 1
                if num < numCoins[ m ]:
                    numCoins[ m ] = num

    return numCoins[ money ]

def main():
    n = int(input())
    coins = [1, 3, 4]
    print(get_change(n, coins))

if __name__ == '__main__':
    main()
