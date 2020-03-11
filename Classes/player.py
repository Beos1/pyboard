class player:
    def __init__(self, playerNumber):
        self.playerNumber = playerNumber
        starting = self.setHome()
        print(starting)
        self.startPosition = starting
        self.Position = [starting, starting,starting,starting]





 

    def setHome(self):
        if self.playerNumber == 1:
            return 112
        elif self.playerNumber == 2:
            return 115
        elif self.playerNumber == 3:
            return 113
        elif self.playerNumber == 4:
            return 116
        elif self.playerNumber == 5:
            return 114
        else:
            return 117
    def getAllPositions(self):
        allPositions = []
        for position in self.Position:
            print(position)
            allPositions.append(position)
        return allPositions
    def setNewPosition(self, newPos, number):
        if number == 1:
            self.Position[0] = newPos
        elif number == 2:
            self.Position[1] = newPos
        elif number == 3:
            self.Position[3] = newPos
        elif number == 4:
            self.Position[3] = newPos
