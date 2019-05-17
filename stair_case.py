#!/bin/python3

import sys

i = 0


def print_hashtag(n, i):
    i += 1
    print(' ' * (n - i) + '#' * i)
    if i == n:
        return
    print_hashtag(n, i)

n = int(input().strip())

print_hashtag(n, i)
