#!/bin/python3

import sys

def make_change(coins, n):
    solutions = [1] + [0] * n
    for coin in coins:
        for index in range(n+1-coin):
            solutions[index+coin] += solutions[index]

    return solutions[n]
    

n,m = input().strip().split(' ')
n,m = [int(n),int(m)]
coins = [int(coins_temp) for coins_temp in input().strip().split(' ')]
print(make_change(coins, n))
