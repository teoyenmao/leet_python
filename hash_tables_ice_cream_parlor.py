#!/bin/python3
import sys

final_ans = []

# Tip: refer to TwoSum: https://leetcode.com/articles/two-sum/

def solve(arr, money):
    # use one-pass hash table
    map_cost = {}
    for i, v in enumerate(arr):
        compliment = money - v
        if compliment in map_cost:
            ans = sorted((map_cost[compliment], i))
            print(ans[0]+1, ans[1]+1)
        else:
            map_cost[v] = i

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        money = int(input().strip())
        n = int(input().strip())
        arr = list(map(int, input().strip().split(' ')))
        solve(arr, money)

    # for x, y in final_ans:
    #     print(x+1, y+1)


# t = int(input().strip())
# for a0 in range(t):
#     m = int(input().strip())
#     n = int(input().strip())
#     a = list(map(int, input().strip().split(' ')))
#
#     # find matched number
#     cost_map = {}
#     for i, cost in enumerate(a):
#         sunny = cost
#         johnny = m - cost
#         if johnny in cost_map.keys():
#             print(cost_map[johnny]+1, i+1)
#         else:
#             cost_map[cost] = i
