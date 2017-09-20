import sys

N = int(input().strip())

print(("Weird", "Not Weird")[N%2 ==0 and (N<5 or N>20)])
