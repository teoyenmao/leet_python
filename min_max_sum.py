#!/bin/python3

import sys

arr = list(map(int, input().strip().split(' ')))

l = max(arr)
s = min(arr)

l_list = list.copy(arr)
del l_list[l_list.index(s)]
s_list = list.copy(arr)
del s_list[s_list.index(l)]

l_sum = sum(l_list)
s_sum = sum(s_list)

print('%d %d' % (s_sum,l_sum))
