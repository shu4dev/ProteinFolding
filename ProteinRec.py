Maxpts = 0

def print2D(array):
     for i in range(13):
            for j in range(13):
                print(array[i][j], end=' ')
            print()

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
    if grid[x][y] != "x":
        return False
    return True

def ProteinFolding(Acidseq, grid, Curnum, x_move, y_move, x, y, pts):
    if Curnum == len(Acidseq) + 1:
        return pts

    for i in range(4):

        x_new = x + x_move[i]

        y_new = y + y_move[i]
    
    if isValid(grid, x_new, y_new):

        grid[x_new][y_new] = Acidseq[Curnum]
        Curnum = Curnum + 1
        pts += Checkpts(grid, x_new, y_new)
        if ProteinFolding(Acidseq, grid, Curnum, x_move, y_move, x_new, y_new, pts):
            return pts
    return False

def solver():
    Acidseq = [0,1,1,0]
    grid = [["x" for i in range(8)] for j in range(8)]
    x_move = [1,-1,0,0]
    y_move = [0,0,1,-1]
    grid[4][4] = Acidseq[0]
    if ProteinFolding(Acidseq, grid, 1, x_move, y_move, 6, 6, 0):
        print()
        print2D(grid)

if __name__ == "__main__":
    solver()