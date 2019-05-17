#!/bin/python3

import sys


def canConstruct(a):
    # Return "Yes" or "No" denoting whether you can construct the required number.
    s = ''.join([str(i) for i in a])
    s = list(s.replace('0', ''))
    for i in s:
        if int(i) % 3 == 0:
            s.pop(s.index(i))
            s.append(i)
            break
    int_v = int(''.join(s))

    return "Yes" if int_v % 3 == 0 else "No"


if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        a = list(map(int, input().strip().split(' ')))
        result = canConstruct(a)
        print(result)
