#!/bin/python3

import sys

def lonely_integer(a):
    occ = {}

    for token in a:
        if token in occ:
            occ[token] = 1 if token in occ else occ[token] + 1

    for key in occ:
        if occ[key] == 1:
            return key
    return None
    

n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]
print(lonely_integer(a))
