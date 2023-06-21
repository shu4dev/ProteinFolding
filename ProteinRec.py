solution = []   
    
def CreateBoard(Acid):
    length = (len(Acid) * 2) + 1
    arr = [[" " for i in range(length)] for j in range(length)]
    return arr

def print2D(array):
    for row in array:
        print(row)
def Checkpts(grid, x, y):
    if (grid[x][y] == 0 and grid[x + 1][y] == 0):
        return 1
    elif (grid[x][y] == 0 and grid[x - 1][y] == 0):
        return 1
    elif (grid[x][y] == 0 and grid[x ][y + 1] == 0):
        return 1
    elif (grid[x][y] == 0 and grid[x][y - 1] == 0):
        return 1  
    return 0

def isValid(grid, x, y):
    if grid[x + 1][y] != " " and grid[x - 1][y] != " " and grid[x][y + 1] and grid[x][y - 1]:
        return False
    return True

def ProteinFolding(Acidseq, grid, Curnum, x_move, y_move, x, y, pts):
    if Curnum == len(Acidseq):
        return True
    for i in range(4):
        x_new = x + x_move[i]
        y_new = y + y_move[i]
    
    if isValid(grid, x_new, y_new):
        grid[x_new][y_new] = Acidseq[i]

    return False

def solver(Acidseq):
    x_cen, y_cen = len(Acidseq), len(Acidseq)
    board = CreateBoard(Acidseq)
    board[x_cen][y_cen] = Acidseq[0]
    
    return 0

if __name__ == "__main__":
    solver([0,1,1,0])