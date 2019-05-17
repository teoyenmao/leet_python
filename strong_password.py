#!/bin/python3

import sys


numbers = "0123456789"
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_characters = "!@#$%^&*()-+"


def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    lack_digits = 0

    has_numeric = False
    has_lower = False
    has_upper = False
    has_special = False
    for c in password:
        if not has_numeric and c.isnumeric():
            has_numeric = True
        elif not has_lower and c.islower():
            has_lower = True
        elif not has_upper and c.isupper():
            has_upper = True
        elif not has_special and c in special_characters:
            has_special = True
    if not has_numeric:
        lack_digits += 1
    if not has_lower:
        lack_digits += 1
    if not has_upper:
        lack_digits += 1
    if not has_special:
        lack_digits += 1

    if n < 6:   # password is too short
        x = 6 - n
        if lack_digits < x:
            return x

    return lack_digits


if __name__ == "__main__":
    n = int(input().strip())
    password = input().strip()
    answer = minimumNumber(n, password)
    print(answer)
