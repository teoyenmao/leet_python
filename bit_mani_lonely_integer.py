#!/bin/python3

import sys
from collections import defaultdict

def lonely_integer(a):

    # Note: This is not bit manipulation
    # integer_dicts = defaultdict(int)
    # for i in a:
    #     integer_dicts[i] += 1
    #
    # for x in integer_dicts:
    #     if integer_dicts[x] % 2 != 0:
    #         return x

    # Note:
    # v ^ 0 -> v;  v ^ v -> 0
    v = 0
    for i in a:
        v ^= i
    return v

n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]
print(lonely_integer(a))
