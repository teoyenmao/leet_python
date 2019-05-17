#!/bin/python3

# import sys
#
# sys.setrecursionlimit(1000000000000)


c = 3
ci = 3
t_check = 1

# Error: maximum recursion depth, overflow!!
# def strange_counter(t_out, ci):
#     global t_check, c
#
#     if t_check == t_out:
#         return c
#
#     t_check += 1
#     c -= 1
#     if c == 0:
#         ci = ci * 2
#         c = ci
#
#     #print("c %d, ci %d, t_check %d" %(c, ci, t_check))
#
#     return strange_counter(t_out, ci)

def strange_counter(t):
    rem = 3
    while t > rem:
        t = t-rem
        rem *= 2
        print("t %d, rem %d" % (t, rem))

    return rem - t + 1

    # while t > ci:
    #     t -= 1
    #     ci += 1
    # ci *= 2




t = int(input().strip())

# ret = strange_counter(t, ci)
ret = strange_counter(t)
print(ret)




# in: 32434,            out: 16716
# in: 1000000000000,    out: 649267441662
# in: 999999997668,     out: 649267443994
# in: 999999766777,     out: 649267674885
# in: 99999997668,      out: 3079217434
