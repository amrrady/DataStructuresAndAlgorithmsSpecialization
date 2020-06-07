#!/usr/bin/env python3

import math
import random
import sys

class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x} ,{self.y})"


def euclideanDistance(p1, p2):
    return math.sqrt((p1.x - p2.x) * 
                     (p1.x - p2.x) +
                     (p1.y - p2.y) * 
                     (p1.y - p2.y))

def truncate(f, n):
    return math.floor(f * 10 ** n) / 10 ** n

def closestPairDistanceBruteForce(data):
    n = len(data)
    minDistance = sys.maxsize
    for i in range(n):
        for j in range(i+1, n):
            d = euclideanDistance(data[i], data[j])
            if d < minDistance:
                minDistance = d

    return minDistance


def closestStrip(strip, d):
    strip.sort(key=lambda point:point.y)
    nStrip = len(strip)
    minDistance = d
    for i in range(nStrip):
        for j in range(i+1, nStrip):
            if abs(strip[i].y - strip[j].y) < minDistance:
                minDistance = euclideanDistance(strip[i], strip[j])
    
    return minDistance

def closestDivide(Px, Py):
    n = len(Px)
    if n <= 3:
        return closestPairDistanceBruteForce(Px)

    mid      = n // 2
    midPoint = Px[mid]
    Lx       = Px[:mid]
    Rx       = Px[mid:]

    Ly,Ry = [], []
    for i in Py:
        if i.x < midPoint.x:
            Ly.append(i)
        else:
            Ry.append(i)

    minDistanceLeft  = closestDivide(Lx, Ly)
    minDistanceRight = closestDivide(Rx, Ry)
    minDistance = min(minDistanceLeft, minDistanceRight)

    #strip
    Sy = []
    for i in Py:
        if (midPoint.x - minDistance) < i.x and i.x < (midPoint.x + minDistance) :
            Sy.append(i)
    
    for i in range(len(Sy) - 1):
        for j in range(i+1, min(i + 7, len(Sy))):
            dist = euclideanDistance(Sy[i], Sy[j])
            if dist < minDistance:
                minDistance = dist
    return minDistance


def merge(left, right, attr):
    i, j = 0, 0
    combined = []
    while i < len(left) and j < len(right):
        if getattr(left[i], attr) < getattr(right[j], attr):
            combined.append(left[i])
            i += 1
        else:
            combined.append(right[j])
            j += 1
    
    while i <  len(left):
        combined.append(left[i])
        i += 1

    while j <  len(right):
        combined.append(right[j])
        j += 1
    
    return combined

def mergeSort(data, attr):
    if len(data) == 1:
        return data
    
    mid   = len(data) // 2
    left  = mergeSort(data[:mid], attr)
    right = mergeSort(data[mid:], attr)
    return merge(left, right, attr)

def initSort(data):
    Px = mergeSort(data,'x')
    Py = mergeSort(data,'y')
    return Px,Py

def closestPair(data):
    Px, Py = initSort(data)
    return closestDivide(Px,Py)

def main():
    n = int(input())

    data = []
    for i in range(n):
        x,y = map(int, input().split())
        data.append(Point(x,y))

    print(closestPair(data))


if __name__ == "__main__":
    main()