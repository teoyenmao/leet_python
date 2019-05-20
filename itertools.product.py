#!/bin/python3

from itertools import product

# a = input().strip().split(' ')
# b = input().strip().split(' ')

a = [1, 2]
b = [3, 4]
# expect result: (1, 3) (1, 4) (2, 3) (2, 4)

# p_result = list(product(a, b))
# result = ''
# for i, x in enumerate(p_result):
#     result += '('
#     for j, y in enumerate(x):
#         comma = ', ' if j < len(x) - 1 else ''
#         result = result + str(y) + comma
#     space = ' ' if i < len(p_result) - 1 else ''
#     result = result + ')' + space

# print(result)

# SIMPLER ANSWER
print(*product(a, b))
