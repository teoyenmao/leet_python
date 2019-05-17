#!/bin/python3


def plus_minus(arr):
    pos, neg, zero = 0, 0, 0
    for v in arr:
        if v > 0:
            pos += 1
        elif v < 0:
            neg += 1
        else:
            zero += 1

    pos = pos / len(arr)
    neg = neg / len(arr)
    zero = zero / len(arr)

    return pos, neg, zero

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
#print(arr)

pos, neg, zero = plus_minus(arr)
print("%.4f" % pos)
print("%.4f" % neg)
print("%.4f" % zero)
