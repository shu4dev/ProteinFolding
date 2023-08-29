import copy
import matplotlib.pyplot as plt

maxScore = 0
fig = 0
ax = 0
BestFold = []
twoDimLabbyfoldKeys = ["W", "D", "S", "A"]
threeDimLabbyfoldKeys = ["W", "D", "S", "A", "F", "E"]
fourDimLabbyfoldKeys = ["W", "D", "S", "A", "F", "E", "G", "R"]
hexfoldKeys = ["W", "E", "D", "X", "Z", "A"]


# This function produces the next set of possible Coordinates that the next acid can be placed.
# currentCoords: [x,y] or [x, y, z] position of the latest acid.
# prevCoord: [x,y] or [x, y, z] position of the previous acid.
# foldType: the type of fold.  Accepted: "2D Labbyfold", "Hexfold", "3D Labbyfold", "4D Labbyfold"
def getNextCoords(currentCoords, foldType):
    possibleCoords = []
    if foldType == "2D Labbyfold":
        possibleCoords = [
            [currentCoords[0], currentCoords[1] + 1],
            [currentCoords[0] + 1, currentCoords[1]],
            [currentCoords[0], currentCoords[1] - 1],
            [currentCoords[0] - 1, currentCoords[1]],
        ]
    elif foldType == "Hexfold":
        if (currentCoords[1] % 2) == 0:
            possibleCoords = [
                [currentCoords[0] - 1, currentCoords[1] + 1],
                [currentCoords[0], currentCoords[1] + 1],
                [currentCoords[0] + 1, currentCoords[1]],
                [currentCoords[0], currentCoords[1] - 1],
                [currentCoords[0] - 1, currentCoords[1] - 1],
                [currentCoords[0] - 1, currentCoords[1]],
            ]
        elif (currentCoords[1] % 2) == 1:
            possibleCoords = [
                [currentCoords[0], currentCoords[1] + 1],
                [currentCoords[0] + 1, currentCoords[1] + 1],
                [currentCoords[0] + 1, currentCoords[1]],
                [currentCoords[0] + 1, currentCoords[1] - 1],
                [currentCoords[0], currentCoords[1] - 1],
                [currentCoords[0] - 1, currentCoords[1]],
            ]
    elif foldType == "3D Labbyfold":
        possibleCoords = [
            [currentCoords[0], currentCoords[1] + 1, currentCoords[2]],
            [currentCoords[0] + 1, currentCoords[1], currentCoords[2]],
            [currentCoords[0], currentCoords[1] - 1, currentCoords[2]],
            [currentCoords[0] - 1, currentCoords[1], currentCoords[2]],
            [currentCoords[0], currentCoords[1], currentCoords[2] + 1],
            [currentCoords[0], currentCoords[1], currentCoords[2] - 1],
        ]
    elif foldType == "4D Labbyfold":
        possibleCoords = [
            [currentCoords[0], currentCoords[1] + 1, currentCoords[2], currentCoords[3]],
            [currentCoords[0] + 1, currentCoords[1], currentCoords[2], currentCoords[3]],
            [currentCoords[0], currentCoords[1] - 1, currentCoords[2], currentCoords[3]],
            [currentCoords[0] - 1, currentCoords[1], currentCoords[2], currentCoords[3]],
            [currentCoords[0], currentCoords[1], currentCoords[2] + 1, currentCoords[3]],
            [currentCoords[0], currentCoords[1], currentCoords[2] - 1, currentCoords[3]],
            [currentCoords[0], currentCoords[1], currentCoords[2], currentCoords[3]+1],
            [currentCoords[0], currentCoords[1], currentCoords[2], currentCoords[3]-1],
        ]
    return possibleCoords


def CoordsIsValid(Coords, listOfCoords):
    for i in range(len(listOfCoords)):
        if Coords == listOfCoords[i]:
            return False
    return True


def countScore(acidSeq, listOfCoords, foldType):
    copyListOfCoords = listOfCoords.copy()
    score = 0
    for Coord in copyListOfCoords:
        i = listOfCoords.index(Coord)  # the index of Coord in copyListOfCoords
        for PossCoord in getNextCoords(Coord, foldType):
            if not CoordsIsValid(PossCoord, copyListOfCoords):  # PossCoord is in listOfCoords
                j = listOfCoords.index(PossCoord)
                if acidSeq[i] == 0 and acidSeq[j] == 0 and (not (((j - i) == 1) or ((i - j) == 1))):
                    score = score + 1
    return int(score / 2)


# This is the initial starter function that takes in a acidSeq and foldType and prints the fold type, score, and
#     the steps required to get that score if it is equal or greater than the current best score.
# acidSeq: the input of array of 0 or 1.
# foldType: the type of fold.  Accepted: "2D Labbyfold", "Hexfold", "3D Labbyfold", "4D Labbyfold"
def ProteinFolding(acidSeq, foldType):
    foldSeq = ["D"]
    CoordsOfFolds = [[0, 0], [1, 0]]
    if foldType == "2D Labbyfold" or foldType == "Hexfold":
        CoordsOfFolds = [[0, 0], [1, 0]]
        fold(acidSeq, foldType, foldSeq, CoordsOfFolds)
    elif foldType == "3D Labbyfold":
        CoordsOfFolds = [[0, 0, 0], [1, 0, 0]]
        fold(acidSeq, foldType, foldSeq, CoordsOfFolds)
    elif foldType == "4D Labbyfold":
        CoordsOfFolds = [[0, 0, 0, 0], [1, 0, 0, 0]]
        fold(acidSeq, foldType, foldSeq, CoordsOfFolds)
    else:
        print("Invalid fold type parameter. Accepted: \"2D Labbyfold\", \"Hexfold\", \"3D Labbyfold\", \"4D Labbyfold\"")


# This function takes in an acidSeq, score, foldSeq, and CoordsOfFolds uses recursion to print the foldSeq if the
#     current score is greater than the max score.
# acidSeq: the input of array of 0 or 1.
# foldType: the type of fold.  Accepted: "2D Labbyfold", "Hexfold", "3D Labbyfold"
# score: an int that represent how many folds that has pairs of 0s next to each other
# CoordsOfFolds: an array of the current Coordinates of the acid structure
def fold(acidSeq, foldType, foldSeq, listOfCoords):
    global maxScore
    global BestFold
    if len(foldSeq) >= (len(acidSeq) - 1):
        score = countScore(acidSeq, listOfCoords, foldType)
        if score >= maxScore:
            maxScore = score
            BestFold = copy.copy(listOfCoords)
            print(foldType + " with a score of " + str(score) + ". Moves made: " + str(foldSeq) + ". List of Coordinates: " + str(listOfCoords))
        return
    listNextCoords = getNextCoords(listOfCoords[(len(listOfCoords) - 1)], foldType)
    for possCoord in listNextCoords:
        i = listNextCoords.index(possCoord)
        valid = CoordsIsValid(possCoord, listOfCoords)
        if valid:
            if foldType == "Hexfold":
                fold(acidSeq, foldType, foldSeq + [hexfoldKeys[i]], listOfCoords + [possCoord])
            elif foldType == "2D Labbyfold":
                fold(acidSeq, foldType, foldSeq + [twoDimLabbyfoldKeys[i]], listOfCoords + [possCoord])
            elif foldType == "3D Labbyfold":
                fold(acidSeq, foldType, foldSeq + [threeDimLabbyfoldKeys[i]], listOfCoords + [possCoord])
            elif foldType == "4D Labbyfold":
                fold(acidSeq, foldType, foldSeq + [fourDimLabbyfoldKeys[i]], listOfCoords + [possCoord])
    return


def plotAcid(listOFCoords, foldType):
    global fig
    global ax
    fig = plt.figure()
    x = []
    y = []
    z = []
    if foldType == "3D Labbyfold":
        ax = plt.axes(projection='3d')
        for coord in listOFCoords:
            x.append(coord[0])
            y.append(coord[1])
            z.append(coord[2])
        ax.scatter3D(x, y, z, color='red')
        ax.plot3D(x, y, z)
        ax.set_xlabel('X-axis')
        ax.set_ylabel('Y-axis')
        ax.set_zlabel('Z-axis')
    elif foldType == "2D Labbyfold":
        ax = plt.axes()
        for coord in listOFCoords:
            x.append(coord[0])
            y.append(coord[1])
        ax.scatter(x, y, color='red')
        ax.plot(x, y)
        ax.set_xlabel('X-axis')
        ax.set_ylabel('Y-axis')
    elif foldType == "Hexfold":
        print("Hexfold cannot be plotted on a graph. This function can only plot \"2D Labbyfold\" and \"3D Labbyfold\"")
    plt.show()
    return


# sequence = [0, 1, 0, 1, 0, 0, 1]
sequence = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0]  # score of 9
sequence1 = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1]  #
# print(len(sequence))

# ProteinFolding(sequence, '2D Labbyfold')
ProteinFolding(sequence1, 'Hexfold')

# plotAcid(BestFold, '2D Labbyfold')
