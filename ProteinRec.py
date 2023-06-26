input  = [0,1,1,0]
grid   = [[" " for i in range(2 * len(input) + 1)] for j in range(2 * len(input) + 1)]
Maxpts = 0
grid[4][4] = input[0]

def print2D(array):
     for i in range(9):
            for j in range(9):
                print(grid[i][j], end=' ')
            print()

def Checkpts(grid, y, x, direc):
    if direc == "R":
        if (grid[y][x] == 0 and grid[y + 1][x] == 0):
            return 1
        elif (grid[y][x] == 0 and grid[y - 1][x] == 0):
            return 1
        if (grid[y][x] == 0 and grid[y][x - 1] == 0):
            return 1
        else:
            return 0
    elif direc == "L":
        if (grid[y][x] == 0 and grid[y + 1][x] == 0):
            return 1
        elif (grid[y][x] == 0 and grid[y - 1][x] == 0):
            return 1
        elif (grid[y][x] == 0 and grid[y][x + 1] == 0):
            return 1
        else:
            return 0
    elif direc == "U":
        if (grid[y][x] == 0 and grid[y - 1][x] == 0):
            return 1
        elif (grid[y][x] == 0 and grid[y - 1][x - 1] == 0):
            return 1
        elif (grid[y][x] == 0 and grid[y][x + 1] == 0):
            return 1
        else:
            return 0
    elif direc == "D":
        if (grid[y][x] == 0 and grid[y + 1][x] == 0):
            return 1
        elif (grid[y][x] == 0 and grid[y - 1][x - 1] == 0):
            return 1
        elif (grid[y][x] == 0 and grid[y][x + 1] == 0):
            return 1
        else:
            return 0
    return 0

def isValid(grid, y, x):
    if grid[y][x] == " ":
        return True
    return False

def ProteinFolding(Acidseq, grid, Curnum, y_move, x_move, y, x, pts, direc):

    if Curnum == len(Acidseq):
        print2D(grid)
        return pts
    
    for i in range(4):
        
        y_new = y + y_move[i]
        x_new = x + x_move[i]
        
        if isValid(grid, y_new, x_new):

            grid[y_new][x_new] = Acidseq[Curnum]
            pts = pts + Checkpts(grid, y_new, x_new, direc[i])
            if ProteinFolding(Acidseq, grid, Curnum + 1, y_move, x_move, y_new, x_new, pts, direc) > 0:
                return True
            grid[y_new][x_new] = " "
    return 0

if __name__ == "__main__":

    y_move = [1,-1,0,0]
    x_move = [0,0,-1,1]
    direc = ["R", "L", "D", "U"]
    # R, L, D, U
    ProteinFolding(input, grid, 1, x_move, y_move, 4, 4 ,0, direc)
    
    print2D(grid)