#!/bin/python3

import sys

def timeConversion(s):
    # Complete this function
    hr = s[:2]
    am_pm = s[8:10]
    if am_pm == 'PM':
        ret_hr = str(int(hr) + 12)
        if hr == '12':
            ret_hr = hr
    else: # 'AM'
        ret_hr = hr
        if hr == '12':
            ret_hr = '00'
    ret_s = str(ret_hr) + s[2:8]
    return ret_s

s = input().strip()
result = timeConversion(s)
print(result)
