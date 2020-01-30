from Classes.player import player, getAllPositions
from Classes.dice import rollDie
from Classes.board import board
from appJar import gui
playerCount = 0
players = []
while(1>=playerCount or playerCount>6):
    playerCount = int(input("How many Players(1-6): "))
newGame = board()
x= 1
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
        if(currentRoll!=1 or 6):
            for x in currentPositions:
                if x == player.startPosition:
                    currentPositions.remove(x)
        for x in currentPositions:
            print(x)
        isThereAWinner=True
print("The winner is player number ")
winner = "me"
print( winner)
#app = gui()
#app.addLabel("title", "Welcome to appJar")
#app.setLabelBg("title", "red")
#app.go()
