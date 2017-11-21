def findSol(n):
    mem = {0:1, 1:1, 2:2}
    findSolDP(n, mem)
    return mem[n]

def findSolDP(n, mem):
    if n in [0, 1, 2]:
        return mem[n]
    else:
        if n not in mem:
            mem[n] = findSolDP(n - 1, mem) + findSolDP(n - 2, mem) + findSolDP(n - 3, mem)
        return mem[n]
    
s = int(input().strip())
for a0 in range(s):
    n = int(input().strip())
    print(findSol(n))
