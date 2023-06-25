input  = [0,1,1,0]
grid   = [[" " for i in range(2 * len(input) + 1)] for j in range(2 * len(input) + 1)]
Maxpts = 0
grid[4][4] = input[0]

def print2D(array):
    for row in array:
        print(row)

def Checkpts(grid, x, y):
    if (grid[x][y] == 0 and grid[x + 1][y] == 0):
        return 1
    elif (grid[x][y] == 0 and grid[x - 1][y] == 0):
        return 1
    elif (grid[x][y] == 0 and grid[x][y + 1] == 0):
        return 1
    elif (grid[x][y] == 0 and grid[x][y - 1] == 0):
        return 1  
    return 0

def isValid(grid, x, y):
    if grid[x][y] != " ":
        return False
    return True

def ProteinFolding(Acidseq, grid, Curnum, x_move, y_move, x, y, pts):

    if Curnum == len(Acidseq):
        return pts
    
    for i in range(4):
        
        x_new = x + x_move[i]
        y_new = y + y_move[i]
    
    if isValid(grid, x_new, y_new):

        pts_new = pts + Checkpts(grid, x_new, y_new)
        grid[x_new][y_new] = Acidseq[Curnum]

        if ProteinFolding(Acidseq, grid, Curnum + 1, x_move, y_move, x_new, y_new, pts_new) > 0:
            print()
            print2D(grid)            
            return True
        grid[x_new][y_new] = " "
        

    return False


if __name__ == "__main__":

    x_move = [-1,1,0,0]
    y_move = [0,0,-1,1]

    ProteinFolding(input, grid, 1, x_move, y_move, 4, 4 ,0)