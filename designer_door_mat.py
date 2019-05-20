#!/bin/python3

import sys


def prepare_door_mat(n, m):
    # Complete this function

    # METHOD 1
    # mid_n = (n // 2)
    # p = '.|.'
    # p_count = 1
    # pl = '-' * m
    # for i in range(n):
    #     if i < mid_n:
    #         p = '.|.' * p_count
    #         m_left = m//2 - len(p)//2
    #         m_right = m//2 + len(p)//2 + 1
    #         pattern = pl[:m_left] + p + pl[m_right:]
    #         p_count += 2
    #     elif i == mid_n:
    #         m_left = m//2 - 7//2
    #         m_right = m//2 + 7//2 + 1
    #         pattern = pl[:m_left] + 'WELCOME' + pl[m_right:]
    #         p_count -= 2
    #     else: # i > mid_n
    #         p = '.|.' * p_count
    #         m_left = m//2 - len(p)//2
    #         m_right = m//2 + len(p)//2 + 1
    #         pattern = pl[:m_left] + p + pl[m_right:]
    #         p_count -= 2
    #     print(pattern)


    # METHOD 2

    p = '.|.'
    p_count = 1
    for i in range(n):
        if i < n//2:
            p = '.|.' * p_count
            pattern = p.center(m, '-')
            p_count += 2
        elif i == n//2:
            pattern = 'WELCOME'.center(m, '-')
            p_count -= 2
        else: # i > n//2
            p = '.|.' * p_count
            pattern = p.center(m, '-')
            p_count -= 2
        print(pattern)

    return

# n, m = map(int, input().strip().split(' '))
n, m = 7, 21
n, m = 11, 33

prepare_door_mat(n, m)
