#!/bin/python3

import sys
import os

roman_dict = {
    1: 'I',
    4: 'IV',
    5: 'V',
    9: 'IX',
    10: 'X',
    40: 'XL',
    50: 'L',
    90: 'XC',
    100: 'C',
    400: 'CD',
    500: 'D',
    900: 'CM',
    1000: 'M'
}


def single_romanizer(d):
    if 1 < d < 4:
        r = d * roman_dict[1]
        ret.append(r)
    elif 5 < d < 9:
        r = roman_dict[5] + roman_dict[1] * (i - 5)
    else:
        r = roman_dict[d]
    return r


def romanizer(numbers):
    ret = []
    for i in numbers:
        if 1 < i < 4:
            r = i * roman_dict[1]
            ret.append(r)
        elif 5 < i < 9:
            r = roman_dict[5] + roman_dict[1] * (i - 5)
            ret.append(r)
        elif 10 < i < 40:
            i_str = str(i)
            r = roman_dict[10] * int(i_str[0]) + single_romanizer(int(i_str[1]))
            ret.append(r)
        elif 40 < i < 50:
            i_str = str(i)
            r = roman_dict[40] + single_romanizer(i_str[1])
            ret.append(r)
        elif 50 < i < 90:
            # TODO
            pass
        elif 90 < i < 100:
            # TODO
            pass
        elif 100 < i < 400:
            # TODO
            pass
        elif 400 < i < 500:
            # TODO
            pass
        elif 500 < i < 900:
            # TODO
            pass
        elif 900 < i < 1000:
            # TODO
            pass
        else:
            ret.append(roman_dict[i])

    return ret

# n = int(input().strip())
# arr = list(map(int, input().strip().split(' ')))

# print(romanizer(arr))
