from Classes.player import player
from Classes.dice import rollDie
from Classes.board import board
from appJar import gui
playerCount = 0
players = []
while(1>=playerCount or playerCount>6):
    playerCount = int(input("How many Players(1-6): "))
newGame = board()
x= 0
# creates a game with the selected number of players between 1 and 6
while(x<playerCount):
    players.append(player(x))
    x = x+1
    print(x)
# for each player creates 4 pieces and placers them in the assigned starting positions
isThereAWinner = False
# A flag for checking if a player has won
currentRoll = 0
currentPositions = []
winner = "me"
while(isThereAWinner==False):
    for player in players:
        currentRoll = rollDie()
        print("You Rolled: ")
        print(currentRoll)
        currentPositions = player.Position
        if(currentRoll!= 1) and (currentRoll!= 6):
            for position in reversed(currentPositions):
                if position == player.startPosition:
                    print("removing: ", position)
                    currentPositions.remove(position)
        if not currentPositions:
            print("No available moves")
        else:            
            print("Choose a piece to move: ")
            i = 0
            for position in reversed(currentPositions): 
                i=i+1
                print(i,": ", position)
            selectedPiece = 0
            while(selectedPiece >= 5 or selectedPiece <= 0): 
                selectedPiece= int(input("Select object to move: "))
            currentPositions[selectedPiece-1]=currentPositions[selectedPiece-1]+currentRoll
            if currentPositions[selectedPiece-1]>80:
                currentPositions[selectedPiece-1]=currentPositions[selectedPiece-1]-80
                print(currentPositions[selectedPiece-1])
                player.setNewPosition(currentPositions[selectedPiece-1], selectedPiece)
                for position in player.Position:
                    if position >= 80:
                        isThereAWinner = True
                        winner = player.playerNumber
    
print("The winner is player number ")
print( winner)
#app = gui()
#app.addLabel("title", "Welcome to appJar")
#app.setLabelBg("title", "red")
#app.go()
