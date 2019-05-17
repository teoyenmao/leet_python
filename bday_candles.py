#!/bin/python3

import sys

def birthdayCakeCandles(n, ar):
    # Complete this function
    tallest = max(ar)
    return ar.count(tallest)

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = birthdayCakeCandles(n, ar)
print(result)
