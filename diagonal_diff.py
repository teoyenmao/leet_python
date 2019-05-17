#!/bin/python3

import sys


def diagonal_diff(a):
    x, y = 0, 0
    ix, iy = 0, len(a)-1
    for l in a:
        x += l[ix]
        y += l[iy]
        if ix < len(a) and iy >= 0:
            ix += 1
            iy -= 1

    return abs(x - y)

n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)

# print(a)

print(diagonal_diff(a))
