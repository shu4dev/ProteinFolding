maxScore = 0
twoDimLabbyfoldKeys = ["W", "D", "S", "A"]
threeDimLabbyfoldKeys = ["W", "D", "S", "A", "F", "E"]
hexfoldKeys = ["W", "E", "D", "X", "Z", "A"]


# This function produces the next set of possible coordinates that the next acid can be placed.
# currentcoords: [x,y] or [x, y, z] position of the latest acid.
# prevcoord: [x,y] or [x, y, z] position of the previous acid.
# foldType: the type of fold.  Accepted: "2D Labbyfold", "Hexfold", "3D Labbyfold"
def getNextcoords(currentcoords, foldType):
    possiblecoords = []
    if foldType == "2D Labbyfold":
        possiblecoords = [
            [currentcoords[0], currentcoords[1] + 1],
            [currentcoords[0] + 1, currentcoords[1]],
            [currentcoords[0], currentcoords[1] - 1],
            [currentcoords[0] - 1, currentcoords[1]],
        ]
    elif foldType == "Hexfold":
        possiblecoords = 0
        if (currentcoords[0] % 2) == 0:
            possiblecoords = [
                [currentcoords[0] - 1, currentcoords[1] + 1],
                [currentcoords[0], currentcoords[1] + 1],
                [currentcoords[0] + 1, currentcoords[1]],
                [currentcoords[0], currentcoords[1] - 1],
                [currentcoords[0] - 1, currentcoords[1] - 1],
                [currentcoords[0] - 1, currentcoords[1]],
            ]
        elif (currentcoords[0] % 2) == 1:
            possiblecoords = [
                [currentcoords[0], currentcoords[1] + 1],
                [currentcoords[0] + 1, currentcoords[1] + 1],
                [currentcoords[0] + 1, currentcoords[1]],
                [currentcoords[0] + 1, currentcoords[1] - 1],
                [currentcoords[0], currentcoords[1] - 1],
                [currentcoords[0] - 1, currentcoords[1]],
            ]
    elif foldType == "3D Labbyfold":
        possiblecoords = [
            [currentcoords[0], currentcoords[1] + 1, currentcoords[2]],
            [currentcoords[0] + 1, currentcoords[1], currentcoords[2]],
            [currentcoords[0], currentcoords[1] - 1, currentcoords[2]],
            [currentcoords[0] - 1, currentcoords[1], currentcoords[2]],
            [currentcoords[0], currentcoords[1], currentcoords[2] + 1],
            [currentcoords[0], currentcoords[1], currentcoords[2] - 1],
        ]
    return possiblecoords


def coordsIsValid(coords, listOfcoords):
    for i in range(len(listOfcoords)):
        if coords == listOfcoords[i]:
            return False
    return True


def countScore(acidSeq, listOfcoords, foldType):
    copyListOfcoords = listOfcoords.copy()
    score = 0
    for coord in copyListOfcoords:
        i = listOfcoords.index(coord)  # the index of coord in copyListOfcoords
        for PossCoord in getNextcoords(coord, foldType):
            if not coordsIsValid(PossCoord, copyListOfcoords):  # Posscoord is in listOfcoords
                j = listOfcoords.index(PossCoord)
                if acidSeq[i] == 0 and acidSeq[j] == 0 and (not (((j - i) == 1) or ((j - i) == 1))):
                    score = score + 1
                    print("i = ", i, " j = ", j)
                    copyListOfcoords.remove(PossCoord)
    return score


# This is the initial starter function that takes in a acidSeq and foldType and prints the fold type, score, and
#     the steps required to get that score if it is equal or greater than the current best score.
# acidSeq: the input of array of 0 or 1.
# foldType: the type of fold.  Accepted: "2D Labbyfold", "Hexfold", "3D Labbyfold"
def ProteinFolding(acidSeq, foldType):
    foldSeq = ["D"]
    coordsOfFolds = [[0, 0], [1, 0]]
    if foldType == "2D Labbyfold" or foldType == "Hexfold" or foldType == "3D Labbyfold":
        fold(acidSeq, foldType, foldSeq, coordsOfFolds)
    else:
        print("Invalid fold type parameter. Accepted: \"2D Labbyfold\", \"Hexfold\", \"3D Labbyfold\"")


# This function takes in an acidSeq, score, foldSeq, and coordsOfFolds uses recursion to print the foldSeq if the
#     current score is greater than the max score.
# acidSeq: the input of array of 0 or 1.
# foldType: the type of fold.  Accepted: "2D Labbyfold", "Hexfold", "3D Labbyfold"
# score: an int that represent how many folds that has pairs of 0s next to each other
# coordsOfFolds: an array of the current coordinates of the acid structure
def fold(acidSeq, foldType, foldSeq, listOfcoords):
    global maxScore
    if len(foldSeq) >= (len(acidSeq) - 1):
        score = countScore(acidSeq, listOfcoords, foldType)
        if score >= maxScore:
            maxScore = score
            print(foldType + " with a score of " + str(score) + ". Moves made: " + str(foldSeq) + ". List of coordinates: " + str(listOfcoords))
        return
    listNextcoords = getNextcoords(listOfcoords[(len(listOfcoords) - 1)], foldType)
    for posscoord in listNextcoords:
        i = listNextcoords.index(posscoord)
        valid = coordsIsValid(posscoord, listOfcoords)
        if valid:
            if foldType == "Hexfold":
                foldSeq.append(hexfoldKeys[i])
                listOfcoords.append(posscoord)
                fold(acidSeq, foldType, foldSeq, listOfcoords)
                foldSeq.remove(hexfoldKeys[i])
                listOfcoords.remove(posscoord)
            elif foldType == "2D Labbyfold":
                foldSeq.append(twoDimLabbyfoldKeys[i])
                listOfcoords.append(posscoord)
                fold(acidSeq, foldType, foldSeq, listOfcoords)
                foldSeq.remove(twoDimLabbyfoldKeys[i])
                listOfcoords.remove(posscoord)
            elif foldType == "3D Labbyfold":
                foldSeq.append(threeDimLabbyfoldKeys[i])
                listOfcoords.append(posscoord)
                fold(acidSeq, foldType, foldSeq, listOfcoords)
                foldSeq.remove(threeDimLabbyfoldKeys[i])
                listOfcoords.remove(posscoord)
    return


sequence = [0, 0, 0]
ProteinFolding(sequence, '2D Labbyfold')
