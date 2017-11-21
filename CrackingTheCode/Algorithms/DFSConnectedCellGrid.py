from collections import defaultdict

def reccDFS(grid, row, col, connections):
    if grid[row][col] == 1:
        if col not in connections[row]:
            connections[row].append(col)
            if row < len(grid) - 1:
                reccDFS(grid, row + 1, col, connections)
            if col < len(grid[row]) - 1:
                reccDFS(grid, row, col + 1, connections)
            if row > 0:
                reccDFS(grid, row - 1, col, connections)
            if col > 0:
                reccDFS(grid, row, col - 1, connections)

            if row > 0 and col > 0:
                reccDFS(grid, row - 1, col - 1, connections)
            if row < len(grid) - 1 and col > 0:
                reccDFS(grid, row + 1, col - 1, connections)
            if row > 0 and col < len(grid[row]) - 1:
                reccDFS(grid, row - 1, col + 1, connections)
            if row < len(grid) - 1 and col < len(grid[row]) - 1:
                reccDFS(grid, row + 1, col + 1, connections)
    return 

def treatPath(grid, connections, biggest):
    nbElem = 0
    for row in connections:
        for col in connections[row]:
            grid[row][col] = 0
            nbElem += 1
    connections.clear()
    return nbElem if nbElem > biggest else biggest

def getBiggestRegion(grid):
    biggReggie = 0
    connections = defaultdict(list)

    for i in range(len(grid)):
        row = grid[i]
        for j in range(len(row)):
            if grid[i][j] == 1:
                reccDFS(grid, i, j, connections)
                biggReggie = treatPath(grid, connections, biggReggie)
    return biggReggie

n = int(input().strip())
m = int(input().strip())
grid = []
for grid_i in range(n):
    grid_t = list(map(int, input().strip().split(' ')))
    grid.append(grid_t)

print(getBiggestRegion(grid))

