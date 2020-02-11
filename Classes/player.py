class player:
    def __init__(self, playerNumber):
        self.playerNumber = playerNumber
        starting = setHome(playerNumber)
        self.startPosition = starting
        self.Position = [starting, starting,starting,starting]





 

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
    allPositions.append(player.Position[0])
    allPositions.append(player.Position[1])
    allPositions.append(player.Position[2])
    allPositions.append(player.Position[3])
    return allPositions
def setNewPosition(player, newPos, number):
    if number == 1:
        player.Position[0] = newPos
    elif number == 2:
        player.Position[1] = newPos
    elif number == 3:
        player.Position[3] = newPos
    elif number == 4:
        player.Position[3] = newPos
