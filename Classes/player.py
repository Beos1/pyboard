from marble import marble
class player:
    def __init__(self, playerNumber):
        self.playerNumber = playerNumber
        starting = self.setHome()
        print(starting)
        self.startPosition = starting
        self.marbles = [marble(starting), marble(starting), marble(starting), marble(starting)]
        self.marblesAtHome = 4
        self.colour = self.setPlayerColour()
   
   
   
   
   
    def setHome(self):
    #sets a players home based on the player number assigned to them
        if self.playerNumber == 0:
            return 112
        elif self.playerNumber == 1:
            return 115
        elif self.playerNumber == 2:
            return 113
        elif self.playerNumber == 3:
            return 116
        elif self.playerNumber == 4:
            return 114
        else:
            return 117
    
    
    def setPlayerColour(self):
    #sets a players colour based on the player number assigned to them
        if self.playerNumber == 0:
            return "red"
        elif self.playerNumber == 1:
            return "blue"
        elif self.playerNumber == 2:
            return "green"
        elif self.playerNumber == 3:
            return "yellow"
        elif self.playerNumber == 4:
            return "pink"
        else:
            return "black"

    def getPlayerNumber(self):
    #Returns the player number as a string instead of an int

        return str(self.playerNumber)

    def getAllPositions(self):
    #Returns the positions of all marbles the user has
        allPositions = []
        for position in self.marbles:
            allPositions.append(position)
        return allPositions
        
    def setNewPosition(self, newPos, number):
    #updates the position of a marble 
    # Not currently used
        if number == 1:
            self.marbles[0] = newPos
        elif number == 2:
            self.marbles[1] = newPos
        elif number == 3:
            self.marbles[3] = newPos
        elif number == 4:
            self.marbles[3] = newPos
