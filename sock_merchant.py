#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    total_pairs = 0
    new_ar = []
    for s in ar:
        print(s)
        if s in new_ar:
            new_ar.remove(s)
            total_pairs += 1
            print(" ", total_pairs)
            continue
        new_ar.append(s) # new sock


    print("new_ar", new_ar)
    print(total_pairs)


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # n = int(input())
    # ar = list(map(int, input().rstrip().split()))
    n = 9
    ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]

    result = sockMerchant(n, ar)

    #fptr.write(str(result) + '\n')

    #fptr.close()
