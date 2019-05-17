#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    enter_valley_c = 0
    h = 0
    at_sea_lvl = True
    for i in s:
        at_sea_lvl = h == 0
        if i == 'U':
            h += 1
        elif i == 'D':
            h -= 1
        if at_sea_lvl and i == 'D':
            enter_valley_c += 1

    print("enter_valley_c", enter_valley_c)
    print("height", h)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # n = int(input())
    # s = input()
    n = 12
    s = 'DDUUDDUDUUUD'

    result = countingValleys(n, s)

    # fptr.write(str(result) + '\n')

    # fptr.close()
