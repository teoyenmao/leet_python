#!/bin/python3

import sys
from collections import defaultdict


string = 0
s_dict = defaultdict(int)

def initialize(s):
    # This function is called once before all queries.
    global string, s_dict
    string = s
    # count the characters
    for c in s:
        s_dict[c] += 1
    # print(s_dict)

    palindrome_amt = factorial(len(s)//2)
    print(palindrome_amt)


def factorial(n):
    if n in [0, 1]:
        return n
    return factorial(n-1) + factorial(n-2)


def test_palindrome(sub_s, palindrom_amt):
    print("sub_s", sub_s)
    # odd_amt = 0

    # set_s = set(sub_s)
    # for c in set_s:
    #     count_c = sub_s.count(c)
    #     if count_c % 2 == 1:    # palindrome allow 1 odd only
    #         odd_amt += 1
    #         if odd_amt > 1:
    #             new_sub_s = sub_s[:sub_s.index(c)] + sub_s[sub_s.index(c)+1:]
    #             test_palindrome(new_sub_s, palindrom_amt)
    #
    #
    #
    #
    #
    # return test_palindrome(sub_s[:-1], odd_amt)
    # return odd_amt

def answerQuery(l, r):
    # Return the answer for this query modulo 1000000007.
    l -= 1
    sub_s = string[l:r]
    print(sub_s)

    palindrom_amt = 0
    test_palindrome(sub_s, palindrom_amt)
    print(palindrom_amt)
    # set_s = set(sub_s)
    # for c in set_s:
    #     count_c = sub_s.count(c)
    #     if count_c % 2 == 1:
    #         odd_amt += 1
    #         if odd_amt > 1:
    #             return 0
    # return odd_amt

    # print(sub_s)

if __name__ == "__main__":
    s = input().strip()
    initialize(s)
    q = int(input().strip())
    for a0 in range(q):
        l, r = input().strip().split(' ')
        l, r = [int(l), int(r)]
        result = answerQuery(l, r)
        print(result)
