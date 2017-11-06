# Simple rec without dynamic programming
def fibonacci(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)
    # Write your code here.
n = int(input())
print(fibonacci(n))
