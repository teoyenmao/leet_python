#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the equalizeArray function below.
def equalizeArray(arr):
    max_redundant_num, max_count = 0, 0
    for x in set(arr):
        c = arr.count(x)
        if c > max_count:
            max_redundant_num, max_count = x, c

    print("max_redundant_num %d, max_count %d" % (max_redundant_num, max_count))
    min_deletions = len(arr) - max_count
    print("min_deletions", min_deletions)
    return min_deletions


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # n = int(input())
    # arr = list(map(int, input().rstrip().split()))
    n = 5
    arr = [3, 3, 2, 1, 3]
    print(arr)

    result = equalizeArray(arr)

    #fptr.write(str(result) + '\n')
    #fptr.close()
