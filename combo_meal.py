#!/bin/python3

import sys

def profit(b, s, c):
    # Return the fixed profit.
    p = b + s - c
    return p

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        b, s, c = input().strip().split(' ')
        b, s, c = [int(b), int(s), int(c)]
        result = profit(b, s, c)
        print(result)
