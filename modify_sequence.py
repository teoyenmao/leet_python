#!/bin/python3

import sys


def modify_seq(n, ar):
    next_v = None
    prev_v = None
    c = 1
    ret = 0
    for v in ar:
        if next_v is None:  # 1st time
            prev_v = v
            next_v = v + 1
            print("1st prev_v %d, next_v %d" % (prev_v, next_v))
            continue

        if v < next_v:  # not increasing seq
            ret += 1
            if v == prev_v:
                next_v += 1
            elif v > prev_v:
                next_v += 1
                prev_v = v

        elif v == next_v:
            prev_v = v
            next_v += 1
        else:   # v > next_v
            prev_v = v
            next_v = prev_v + 1
        print("test v %d, ret %d, prev_v %d, next_v %d" % (v, ret, prev_v, next_v))

    return ret

n = int(input().strip())
str_i = input().strip()
str_l = str_i.split(' ')
ar = list(map(int, str_l))
# ar = list(map(int, input().strip().split(' ')))
result = modify_seq(n, ar)
print(result)
