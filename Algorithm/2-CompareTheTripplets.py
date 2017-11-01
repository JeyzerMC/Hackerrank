#!/bin/python3

import sys

def solve(a0, a1, a2, b0, b1, b2):
    a, b = 0, 0
    arrA,arrB = [a0, a1, a2], [b0, b1, b2]
    
    for i in range(3):
        if arrA[i] < arrB[i]:
            b+= 1
        elif arrA[i] > arrB[i]:
            a+= 1
    return [a, b]

a0, a1, a2 = input().strip().split(' ')
a0, a1, a2 = [int(a0), int(a1), int(a2)]
b0, b1, b2 = input().strip().split(' ')
b0, b1, b2 = [int(b0), int(b1), int(b2)]
result = solve(a0, a1, a2, b0, b1, b2)
print (" ".join(map(str, result)))
