#!/bin/python3
import sys

def findMedian(arr):
    lgt = len(arr)
    lgtD = int((lgt - 1) / 2)
    if lgt % 2 == 0:
        return float((arr[lgtD] + arr[lgtD + 1]) / 2 if lgt is not 1 else arr[lgtD])
    else:
        return float(arr[lgtD])

n = int(input().strip())
a = []
a_i = 0
for a_i in range(n):
    a_t = int(input().strip())
    a.append(a_t)
    print(findMedian(sorted(a)))