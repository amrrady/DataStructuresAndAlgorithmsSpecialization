#!/usr/bin/env python3
import sys

def get_optimal_value(capacity, values_weights):
    values_weights.sort(key = lambda x: x[1], reverse = True)
    item_index = 0
    value = 0
    while capacity != 0:
        if(capacity >= values_weights[item_index][0]):
            capacity -= values_weights[item_index][0]
            value += values_weights[item_index][0] * values_weights[item_index][1]
        elif(capacity > 0):
            value += capacity * values_weights[item_index][1]
            capacity = 0
        else:
            return value

        item_index += 1
        if(item_index == len(values_weights)): return value

    return value


n, capacity = map(int, input().split())

val_wgt = []
for i in range(n):
    v, w = map(int, input().split())
    val_wgt.append((w, v/w))

opt_value = get_optimal_value(capacity, val_wgt)
print("{:.4f}".format(opt_value))
