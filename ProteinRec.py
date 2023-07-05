Maxpts  = 0
y_move  = [-1,1,0,0]
x_move  = [0,0,-1,1]

direc  =  ["U", "D", "L", "R"]
symbol =  ["↑", "↓" ,"←", "→"]

def print2D(grid, len):
     for i in range(len):
            for j in range(len):
                print(grid[i][j], end=' ')
            print()

def CopyArray(init, res, len):
     for i in range(len):
            for j in range(len):
                res[i][j] = init[i][j]
    
def print2Dln(array):
    for row in array:
        print(row)

def Checkpts(grid, y, x, direc):

    if direc == "R":
        try:
            if (grid[y][x] == 0 and grid[y][x + 2] == 0):
                return 1
            elif (grid[y][x] == 0 and grid[y - 2][x] == 0):
                return 1
            if (grid[y][x] == 0 and grid[y + 2][x] == 0):
                return 1
            else:
                return 0
        except:
            return 0
    elif direc == "L":
        try:
            if  (grid[y][x] == 0 and grid[y][x - 2] == 0):
                return 1
            elif (grid[y][x] == 0 and grid[y - 2][x] == 0):
                return 1
            elif (grid[y][x] == 0 and grid[y + 2][x] == 0):
                return 1
            else:
                return 0
        except:
            return 0
    elif direc == "U":
        try:
            if (grid[y][x] == 0 and grid[y - 2][x] == 0):
                return 1
            elif (grid[y][x] == 0 and grid[y][x - 2] == 0):
                return 1
            elif (grid[y][x] == 0 and grid[y][x + 2] == 0):
                return 1
            else:
                return 0
        except:
            return 0
    elif direc == "D":
        try:
            if (grid[y][x] == 0 and grid[y + 2][x] == 0):
                return 1
            elif (grid[y][x] == 0 and grid[y][x - 2] == 0):
                return 1
            elif (grid[y][x] == 0 and grid[y][x + 2] == 0):
                return 1
            else:
                return 0
        except:
            return 0

def isValid(grid, y, x):
    if grid[y][x] == " ":
        return True
    return False

def ProteinFolding(Acidseq, grid, Curnum, y, x, pts, resgrid):
    global Maxpts
    global y_move
    global x_move
    global direc
    if Curnum == len(Acidseq):
        if pts > Maxpts:
            Maxpts = pts
            CopyArray(grid, resgrid, len(grid))
        return resgrid
    
    for i in range(4):
        
        y_prog = y + y_move[i]
        x_prog = x + x_move[i]
        
        y_new = y_prog + y_move[i]
        x_new = x_prog + x_move[i]

        if isValid(grid, y_new, x_new):

            grid[y_prog][x_prog] = symbol[i]
            grid[y_new][x_new] = Acidseq[Curnum]
            pts_new = pts + Checkpts(grid, y_new, x_new, direc[i])
            CopyArray(resgrid, ProteinFolding(Acidseq, grid, Curnum + 1, y_new, x_new, pts_new, resgrid), len(grid))
            grid[y_new][x_new] = " "
            grid[y_prog][x_prog] = " "

    return resgrid


def solve(input):

    length = 4 * (len(input) - 1) + 1
    start = 2 * (len(input) - 1)
    grid      = [[" " for i in range(length)] for j in range(length)]
    resgrid   = [[" " for i in range(length)] for j in range(length)]
    grid[start][start] = input[0]
    print2D(ProteinFolding(input, grid, 1, start, start, 0, resgrid), len(grid))
    print("Max score", Maxpts)
    return True
if __name__ == "__main__":
    solve([0, 0, 0, 0, 0, 0, 0, 0])
