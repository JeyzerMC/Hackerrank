from math import sqrt, ceil

def checkPrime(n):
    if n in {0, 1}:
        return False
    for i in range(2, int(sqrt(n)+1)):
        if n % i == 0:
            return False
    return True


p = int(input().strip())
for a0 in range(p):
    n = int(input().strip())
    print("Prime" if checkPrime(n) else "Not prime")
