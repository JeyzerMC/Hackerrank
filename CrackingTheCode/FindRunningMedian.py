#!/bin/python3
import sys

def findRunningMedian(isEven, elem, curr, left, right):
    if curr == None:                # Case len 1
        curr = left = right = elem
        return float(curr), left, right

    if isEven:   # Even Case
        if left == curr:            # Case len 2 
            if elem < curr:
                left = elem
            else:
                right = elem
        else:                       # Case 3+ 
            if elem > left:
                if elem < curr:
                    left = elem
                    right = curr
                else:
                    #TODO
                    left = curr
            elif elem < right:
                if elem > curr:
                    right = elem
                    left = curr
                else:
                    #TODO
                    left = curr
            
        curr = float((left + right) / 2)
    else:       # Odd Case
        if elem > left and elem < right:
            curr = elem
        elif elem < left:
            curr = left
            left = elem
        elif elem > right:
            curr = right
            right = elem
    return float(curr), left, right


curr, left, right = None, None, None
n = int(input().strip())
a = []
a_i = 0

for a_i in range(n):
    a_t = int(input().strip())
    a.append(a_t)
    curr, left, right = findRunningMedian(len(a) % 2 == 0, a_t, curr, left, right)
    print(float(curr), left, right, sep= ", ")
    # print(curr)