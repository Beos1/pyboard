class player:
    def __init__(self, playerNumber):
        self.playerNumber = playerNumber
        self.possition1 = setHome(playerNumber)
        self.possition2 = setHome(playerNumber)
        self.possition3 = setHome(playerNumber)
        self.possition4 = setHome(playerNumber)
 

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