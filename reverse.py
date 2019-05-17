import numpy as np


def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    # shorter way
    m = -1 if x < 0 else 1
    x = x * m

    n = 0
    while x > 0:
        n = (n * 10) + (x % 10)
        x = x // 10

    bit32 = int(hex(2**31 - 1), 16)
    if n > bit32:
        return 0

    return n * m

    # # check x if is 32-bit
    # if np.int32(x) != x:
    #     return 0
    # y = [i for i in str(x)]
    # z = y
    # if y[0] == '-':
    #   z = y[1:]
    # e = len(z) - 1
    # for s in range(len(z)):
    #     if s >= e:
    #         break
    #     # swap
    #     tmp = z[s]
    #     z[s] = z[e]
    #     z[e] = tmp
    #     s+=1
    #     e-=1
    # ret = ''.join(z)
    # if len(z) != len(y):
    #     ret = '-' + ret
    # ret = int(ret)
    # # check ret if is 32-bit
    # if np.int32(ret) != ret:
    #     return 0
    #
    # return ret



a = 1534236469
print("{}, ret {}".format(a, reverse(a)))
