#!/usr/bin/python

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

def displayPathtoPrincess(n,grid):
    #middle = (int(n/2),int(n/2)-1)[n%2 == 0]
    #startPos = [middle, middle]
    
    startPos = findPrincess(n, grid, 'm')
    posPrincess = findPrincess(n, grid, 'p')
    
    while startPos[0] > posPrincess[0]:
        print("UP")
        startPos[0]-= 1

    while startPos[0] < posPrincess[0]:
        print("DOWN")
        startPos[0]+= 1

    while startPos[1] > posPrincess[1]:
        print("LEFT")
        startPos[1]-= 1    

    while startPos[1] < posPrincess[1]:
        print("RIGHT")
        startPos[1]+= 1
        
                
    
#print all the moves here
m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)
