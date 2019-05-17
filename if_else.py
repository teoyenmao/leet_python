#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    N = 4
    if N % 2:   # odd
        print("Weird")
    else:   # even
        if N in range(2, 6):
            print("Not Weird")
        elif N in range(6, 21):
            print("Weird")
        else:
            print("Not Weird")
        
