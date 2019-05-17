#!/bin/python3

import os
import sys

#
# Complete the dynamicArray function below.
#
def dynamicArray(n, queries):
    seqs = [[], []]
    last_ans = 0
    for l in queries:
        x, y = l[1], l[2]
        i = (x ^ last_ans) % n
        print("seq", i)
        if l[0] == 1:
            seqs[i].append(y)
        else: # 2
            ii = y % len(seq[i])




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nq = input().split()

    n = int(nq[0])

    q = int(nq[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
