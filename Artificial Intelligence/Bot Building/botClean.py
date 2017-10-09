#!/usr/bin/python

def findDirt(posr, posc, board):
    minDist, posI, posJ = -1, -1, -1
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'd':
                distDirt = (i - posr)**2 + (j - posc)**2
                if minDist == -1 or distDirt < minDist:
                    minDist, posI, posJ = distDirt, i, j
                    
    return [posI,posJ]

# Head ends here
def next_move(posr, posc, board):
    d = findDirt(posr, posc, board)
    board[d[0]][d[1]] = '-'
    
    if posr > d[0]:
        print("UP")
    elif posr < d[0]:
        print("DOWN")
    elif posc > d[1]:
        print("LEFT")
    elif posc < d[1]:
        print("RIGHT")
        
    if posr == d[0] and posc == d[1]:
        print("CLEAN")
        
    return

# Tail starts here
if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)
