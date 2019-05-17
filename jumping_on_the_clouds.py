#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    last_i = len(c) - 1
    jump_count = 0
    jumped_i = 0
    for i, val in enumerate(c):
        i = jumped_i
        if i > last_i:
            break
        if (i+2 <= last_i) and c[i+2] == 0:
            jumped_i += 2
            jump_count += 1
        elif (i+1 <= last_i): # c[i+1] == 0
            jumped_i += 1
            jump_count += 1

    print("jumped_i %d, jump_count %d" % (jumped_i, jump_count))
    return jump_count



if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # n = int(input())
    # c = list(map(int, input().rstrip().split()))
    #n = 7
    #c = [0, 0, 1, 0, 0, 1, 0]
    #n = 6
    #c = [0, 1, 0, 0, 1, 0]
    n = 6
    c = [0, 0, 0, 1, 0, 0]

    result = jumpingOnClouds(c)

    # fptr.write(str(result) + '\n')

    # fptr.close()
