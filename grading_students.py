#!/bin/python3

import sys

pass_grade = 40

def solve(grades):
    for i in range(len(grades)):
        g = grades[i]
        thres = 5 - (g % 5)
        new_g = g
        if thres < 3:
            new_g = g + thres   # round up
        if new_g < pass_grade:
            new_g = g
        grades[i] = new_g
    return grades

n = int(input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
   grades_t = int(input().strip())
   grades.append(grades_t)
result = solve(grades)
print ("\n".join(map(str, result)))
