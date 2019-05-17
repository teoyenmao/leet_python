#!/bin/python3

import sys

def flippingBits(N):
    one_s_32bit = 0xFFFFFFFF
    z = N ^ one_s_32bit
    return z

if __name__ == "__main__":
    T = int(input().strip())
    for a0 in range(T):
        N = int(input().strip())
        result = flippingBits(N)
        print(result)
