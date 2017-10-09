# Find the princess position
def findPrincess(n, grid, elem):
    posI = 0
    posJ = 0
    for i in range(0,n):
        for j in range(0,n):
            if grid[i][j] == elem:
                posI = i
                posJ = j
                return [posI, posJ]

    return [-1,-1]

# Find next move
def nextMove(n,r,c,grid):
    posPrincess = findPrincess(n, grid, 'p')

    if r > posPrincess[0]:
        return "UP"
    if r < posPrincess[0]:
        return "DOWN"
    if c > posPrincess[1]:
        return "LEFT"
    if c < posPrincess[1]:
        return "RIGHT"
    return ""

# Main
n = int(input())
r,c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())

print(nextMove(n,r,c,grid))
