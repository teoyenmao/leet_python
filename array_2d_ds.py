#!/bin/python3

import sys


def hourglass_sum(arr):
    sum_results = []
    i, j = 0, 0

    for i in range(0, 6):
        for j in range(0, 6):
            if (i + 2 < 6) and (j + 2 < 6):
                r = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + \
                    arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
                sum_results.append(r)

    return sum_results


arr = []
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)
results = hourglass_sum(arr)
max_sum = max(results)

# print(arr)
# print(results)
print(max_sum)
