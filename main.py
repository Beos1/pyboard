from Classes.player import player, getAllPositions
from Classes.dice import rollDie
from Classes.board import board
from appJar import gui
playerCount = 0
players = []
while(1>=playerCount or playerCount>6):
    playerCount = int(input("How many Players(1-6): "))
newGame = board()
x= 0
while(x<playerCount):
    players.append(player(x))
    x = x+1
    print(x)
isThereAWinner = False
currentRoll = 0
currentPositions = []
while(isThereAWinner==False):
    for player in players:
        currentRoll = rollDie()
        print("You Rolled: ")
        print(currentRoll)
        currentPositions=getAllPositions(player)
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
            for position in currentPositions: 
                i=i+1
                print(i,": ", position)
            selectedPiece = 0
            while(selectedPiece >= 5 or selectedPiece <= 0): 
                selectedPiece= int(input("Select object to move: "))
            currentPositions[selectedPiece]=currentPositions[selectedPiece]+currentRoll
            if currentPositions[selectedPiece]>80:
                currentPositions[selectedPiece]=currentPositions[selectedPiece]-80
                print(currentPositions[selectedPiece])
    
print("The winner is player number ")
winner = "me"
print( winner)
#app = gui()
#app.addLabel("title", "Welcome to appJar")
#app.setLabelBg("title", "red")
#app.go()
