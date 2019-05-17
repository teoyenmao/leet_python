#!/bin/python3


# def array_left_rotation(a, n, k):
#     for c in range(k):
#         a.append(a.pop(0))
#     return a
#
#
# n, k = map(int, input().strip().split(' '))
# a = list(map(int, input().strip().split(' ')))
# answer = array_left_rotation(a, n, k);
# print(*answer, sep=' ')



#!/bin/python3

import sys

def leftRotation(a, d):
    for count in range(d):
        a.append(a.pop(0))
    return a

if __name__ == "__main__":
    n, d = input().strip().split(' ')
    n, d = int(n), int(d)
    a = list(map(int, input().strip().split(' ')))
    result = leftRotation(a, d)
    print(" ".join(map(str, result)))
