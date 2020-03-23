from Classes.marble import marble
class player:
    def __init__(self, playerNumber):
        self.playerNumber = playerNumber
        starting = self.setHome()
        print(starting)
        self.startPosition = starting
        self.marbles = [marble(starting), marble(starting), marble(starting), marble(starting)]





 

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
        for position in self.marbles:
            allPositions.append(position)
        return allPositions
        
    def setNewPosition(self, newPos, number):
        if number == 1:
            self.marbles[0] = newPos
        elif number == 2:
            self.marbles[1] = newPos
        elif number == 3:
            self.marbles[3] = newPos
        elif number == 4:
            self.marbles[3] = newPos
