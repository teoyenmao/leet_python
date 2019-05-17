#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    divisor = len(s)
    quotient, remainder = divmod(n, divisor)
    # It's a memory waste to populate string!!
    #new_s = s * quotient + s[:remainder]
    #print("new_s", new_s)

    # count a
    count_a_in_s = s.count('a')
    count_a_in_r = s[:remainder].count('a')
    count_a = count_a_in_s * quotient + count_a_in_r

    print("count_a", count_a)
    return count_a


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #s = input()
    #n = int(input())
    s = 'aba'
    n = 10
    s = 'a'
    n = 1000000000000

    result = repeatedString(s, n)

    #fptr.write(str(result) + '\n')
    #fptr.close()
