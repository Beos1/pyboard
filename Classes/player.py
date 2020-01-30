class player:
    def __init__(self, playerNumber):
        self.playerNumber = playerNumber
        starting = setHome(playerNumber)
        self.startPosition = starting
        self.possition1 = starting
        self.possition2 = starting
        self.possition3 = starting
        self.possition4 = starting
 

def setHome(playerNumber):
    if playerNumber == 1:
        return 112
    elif playerNumber == 2:
        return 115
    elif playerNumber == 3:
        return 113
    elif playerNumber == 4:
        return 116
    elif playerNumber == 5:
        return 114
    else:
         return 117
def getAllPositions(player):
    allPositions = []
    allPositions.append(player.possition1)
    allPositions.append(player.possition1)
    allPositions.append(player.possition1)
    allPositions.append(player.possition1)
    return allPositions