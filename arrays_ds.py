#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

reverse_arr = arr[::-1]
rev_arr = ' '.join(str(x) for x in reverse_arr)


print(arr)
print(rev_arr)
