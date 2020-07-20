#!/usr/bin/env python3

# START = 0
# POINT = 1
# END = 2


def isPointInSegment(data):
    data.sort(key=lambda p: (p[0], int(p[1])))
    results = {}
    count = 0
    for i in data:
        if i[1] == 0:
            count += 1
        elif i[1] == 1:
            results[i[0]] = count
        elif i[1] == 2:
            count -= 1

    return results


def main():
    n, m = map(int, input().split())

    data = []
    for i in range(n):
        x, y = map(int, input().split())
        data.append((x, 0))
        data.append((y, 2))

    points = list(map(int, input().split()))
    for i in points:
        data.append((i, 1))

    results = isPointInSegment(data)

    print(' '.join(str(results[i]) for i in points))
if __name__ == "__main__":
    main()