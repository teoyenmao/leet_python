#!/bin/python3

import sys

def kangaroo(x1, v1, x2, v2):

    # Too slow!
    # if (x1 < x2 and v1 <= v2) or (x1 <= x2 and v1 < v2):
    #     return 'NO'
    # if x1 > 10000 or x2 > 10000 or v1 > 10000 or v2 > 10000:
    #     return 'NO'
    # print("x1 %d x2 %d, v1 %d, v2 %d" % (x1, x2, v1, v2))
    # if x1 == x2:
    #     return 'YES'
    #
    # return kangaroo(x1+v1, v1, x2+v2, v2)

    if (x1 < x2 and v1 <= v2) or (x1 <= x2 and v1 < v2):
        return 'NO'
    if x1 > 10000 or x2 > 10000 or v1 > 10000 or v2 > 10000:
        return 'NO'

    y = (x1 - x2) % (v2 - v1)
    return 'YES' if y == 0 else 'NO'


x1, v1, x2, v2 = input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
result = kangaroo(x1, v1, x2, v2)
print(result)


# math:
# y = number of jumps
#
# equation:
# x1 + v1 * y = x2 + v2 * y
#
# y = (x1 - x2) / (v2 - v1)
# if y == 0, kangaroo can meet each other!!!



# in:
# 1113 612 1331 610
# out:
# YES
