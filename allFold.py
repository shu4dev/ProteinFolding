maxScore = 0
twoDimLabbyfoldKeys = ["W", "D", "S", "A"]
threeDimLabbyfoldKeys = ["W", "D", "S", "A", "F", "E"]
hexfoldKeys = ["W", "E", "D", "X", "Z", "A"]


# This function produces the next set of possible coordinates that the next acid can be placed.
# currentCords: [x,y] or [x, y, z] position of the latest acid.
# prevCord: [x,y] or [x, y, z] position of the previous acid.
# foldType: the type of fold.  Accepted: "2D Labbyfold", "Hexfold", "3D Labbyfold"
def getNextCords(currentCords, foldType):
    possibleCords = []
    if foldType == "2D Labbyfold":
        possibleCords = [
            [currentCords[0], currentCords[1] + 1],
            [currentCords[0] + 1, currentCords[1]],
            [currentCords[0], currentCords[1] - 1],
            [currentCords[0] - 1, currentCords[1]],
        ]
    elif foldType == "Hexfold":
        possibleCords = 0
        if (currentCords[0] % 2) == 0:
            possibleCords = [
                [currentCords[0] - 1, currentCords[1] + 1],
                [currentCords[0], currentCords[1] + 1],
                [currentCords[0] + 1, currentCords[1]],
                [currentCords[0], currentCords[1] - 1],
                [currentCords[0] - 1, currentCords[1] - 1],
                [currentCords[0] - 1, currentCords[1]],
            ]
        elif (currentCords[0] % 2) == 1:
            possibleCords = [
                [currentCords[0], currentCords[1] + 1],
                [currentCords[0] + 1, currentCords[1] + 1],
                [currentCords[0] + 1, currentCords[1]],
                [currentCords[0] + 1, currentCords[1] - 1],
                [currentCords[0], currentCords[1] - 1],
                [currentCords[0] - 1, currentCords[1]],
            ]
    elif foldType == "3D Labbyfold":
        possibleCords = [
            [currentCords[0], currentCords[1] + 1, currentCords[2]],
            [currentCords[0] + 1, currentCords[1], currentCords[2]],
            [currentCords[0], currentCords[1] - 1, currentCords[2]],
            [currentCords[0] - 1, currentCords[1], currentCords[2]],
            [currentCords[0], currentCords[1], currentCords[2] + 1],
            [currentCords[0], currentCords[1], currentCords[2] - 1],
        ]
    return possibleCords


def cordsIsValid(cords, listOfCords):
    for i in range(len(listOfCords)):
        if cords == listOfCords[i]:
            return False
    return True


def countScore(acidSeq, listOfCords, foldType):
    copyListOfCords = listOfCords.copy()
    score = 0
    for cord in copyListOfCords:
        i = listOfCords.index(cord)  # the index of cord in copyListOfCords
        for PossCord in getNextCords(cord, foldType):
            if not cordsIsValid(PossCord, copyListOfCords):  # PossCord is in listOfCords
                j = listOfCords.index(PossCord)
                if acidSeq[i] == 0 and acidSeq[j] == 0 and (not ((j - i) == 1) or (j - i == 1)):
                    score = score + 1
                    copyListOfCords.remove(PossCord)
    return score


# This is the initial starter function that takes in a acidSeq and foldType and prints the fold type, score, and
#     the steps required to get that score if it is equal or greater than the current best score.
# acidSeq: the input of array of 0 or 1.
# foldType: the type of fold.  Accepted: "2D Labbyfold", "Hexfold", "3D Labbyfold"
def ProteinFolding(acidSeq, foldType):
    foldSeq = ["D"]
    cordsOfFolds = [[0, 0], [1, 0]]
    if foldType == "2D Labbyfold" or foldType == "Hexfold" or foldType == "3D Labbyfold":
        fold(acidSeq, foldType, foldSeq, cordsOfFolds)
    else:
        print("Invalid fold type parameter. Accepted: \"2D Labbyfold\", \"Hexfold\", \"3D Labbyfold\"")


# This function takes in an acidSeq, score, foldSeq, and cordsOfFolds uses recursion to print the foldSeq if the
#     current score is greater than the max score.
# acidSeq: the input of array of 0 or 1.
# foldType: the type of fold.  Accepted: "2D Labbyfold", "Hexfold", "3D Labbyfold"
# score: an int that represent how many folds that has pairs of 0s next to each other
# cordsOfFolds: an array of the current coordinates of the acid structure
def fold(acidSeq, foldType, foldSeq, listOfCords):
    global maxScore
    if len(foldSeq) >= (len(acidSeq) - 1):
        score = countScore(acidSeq, listOfCords, foldType)
        if score >= maxScore:
            maxScore = score
            print(foldType + " with a score of " + str(score) + ". Moves made: " + str(foldSeq) + ". List of coordinates: " + str(listOfCords))
        return
    listNextCords = getNextCords(listOfCords[(len(listOfCords) - 1)], foldType)
    for possCord in listNextCords:
        i = listNextCords.index(possCord)
        valid = cordsIsValid(possCord, listOfCords)
        if valid:
            if foldType == "Hexfold":
                foldSeq.append(hexfoldKeys[i])
                listOfCords.append(possCord)
                fold(acidSeq, foldType, foldSeq, listOfCords)
                foldSeq.remove(hexfoldKeys[i])
                listOfCords.remove(possCord)
            elif foldType == "2D Labbyfold":
                foldSeq.append(twoDimLabbyfoldKeys[i])
                listOfCords.append(possCord)
                fold(acidSeq, foldType, foldSeq, listOfCords)
                foldSeq.remove(twoDimLabbyfoldKeys[i])
                listOfCords.remove(possCord)
            elif foldType == "3D Labbyfold":
                foldSeq.append(threeDimLabbyfoldKeys[i])
                listOfCords.append(possCord)
                fold(acidSeq, foldType, foldSeq, listOfCords)
                foldSeq.remove(threeDimLabbyfoldKeys[i])
                listOfCords.remove(possCord)
    return


sequence = [0, 0, 0, 0]
ProteinFolding(sequence, '2D Labbyfold')
