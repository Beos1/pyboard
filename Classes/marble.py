class marble:
    def __init__(self, startingPosition):
        self.position = startingPosition

    def updatePosition(self, updatedPosition):
        self.position = updatedPosition
    
    def getPosition(self):
        return self.position