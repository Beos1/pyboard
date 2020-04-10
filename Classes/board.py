from tkinter import *
from tkinter import ttk
from player import player
from dice import rollDie
def create_circle(x, y, r, canvasName): #center coordinates, radius
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvasName.create_oval(x0, y0, x1, y1)
def create_coloured_circle(x, y, r, canvasName,colour): #center coordinates, radius
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvasName.create_oval(x0, y0, x1, y1,fill=colour)
def create_board(theBoard):
    #spots 1-5
    create_circle(300, 100, 10, theBoard)
    create_circle(320, 100, 10, theBoard)
    create_circle(340, 100, 10, theBoard)
    create_circle(360, 100, 10, theBoard)
    create_circle(380, 100, 10, theBoard)
    #spots 6-10
    create_circle(380, 120, 10, theBoard)
    create_circle(380, 140, 10, theBoard)
    create_circle(380, 160, 10, theBoard)
    create_circle(380, 180, 10, theBoard)
    create_circle(380, 200, 10, theBoard)
    #spots 11-15 
    create_circle(400, 190, 10, theBoard)
    create_circle(420, 180, 10, theBoard)
    create_circle(440, 170, 10, theBoard)
    create_circle(460, 160, 10, theBoard)
    create_circle(480, 150, 10, theBoard)

    #spots 16-19
    create_circle(490, 170, 10, theBoard)
    create_circle(500, 190, 10, theBoard)
    create_circle(510, 210, 10, theBoard)
    create_circle(520, 230, 10, theBoard)

    #spots 20-24
    create_circle(500, 240, 10, theBoard)
    create_circle(480, 250, 10, theBoard)
    create_circle(460, 260, 10, theBoard)
    create_circle(440, 270, 10, theBoard)
    create_circle(420, 280, 10, theBoard)
    #spots 25-29
    create_circle(440, 290, 10, theBoard)
    create_circle(460, 300, 10, theBoard)
    create_circle(480, 310, 10, theBoard)
    create_circle(500, 320, 10, theBoard)
    create_circle(520, 330, 10, theBoard)
    #spots 30-33
    create_circle(510, 350, 10, theBoard)
    create_circle(500, 370, 10, theBoard)
    create_circle(490, 390, 10, theBoard)
    create_circle(480, 410, 10, theBoard)
    #spots34-38
    create_circle(460, 400, 10, theBoard)
    create_circle(440, 390, 10, theBoard)
    create_circle(420, 380, 10, theBoard)
    create_circle(400, 370, 10, theBoard)
    create_circle(380, 360, 10, theBoard)
    #spots 39-43
    create_circle(380, 380, 10, theBoard)
    create_circle(380, 400, 10, theBoard)
    create_circle(380, 420, 10, theBoard)
    create_circle(380, 440, 10, theBoard)
    create_circle(380, 460, 10, theBoard)
    #spots 44-47
    create_circle(360, 460, 10, theBoard)    
    create_circle(340, 460, 10, theBoard)
    create_circle(320, 460, 10, theBoard)
    create_circle(300, 460, 10, theBoard)
    #spots 48-52
    create_circle(300, 440, 10, theBoard)
    create_circle(300, 420, 10, theBoard)
    create_circle(300, 400, 10, theBoard)
    create_circle(300, 380, 10, theBoard)
    create_circle(300, 360, 10, theBoard)
    #spots 53-57
    create_circle(280, 370, 10, theBoard)
    create_circle(260, 380, 10, theBoard)
    create_circle(240, 390, 10, theBoard)
    create_circle(220, 400, 10, theBoard)
    create_circle(200, 410, 10, theBoard)
    #spots 58-61
    create_circle(190, 390, 10, theBoard)
    create_circle(180, 370, 10, theBoard)
    create_circle(170, 350, 10, theBoard)
    create_circle(160, 330, 10, theBoard)
    #spots 62-65
    create_circle(180, 320, 10, theBoard)
    create_circle(200, 310, 10, theBoard)
    create_circle(220, 300, 10, theBoard)
    create_circle(240, 290, 10, theBoard)
    create_circle(260, 280, 10, theBoard)
    #spots 66-70
    create_circle(240, 270, 10, theBoard)
    create_circle(220, 260, 10, theBoard)
    create_circle(200, 250, 10, theBoard)
    create_circle(180, 240, 10, theBoard)
    create_circle(160, 230, 10, theBoard)
    #spots 71-74
    create_circle(170, 210, 10, theBoard)
    create_circle(180, 190, 10, theBoard)
    create_circle(190, 170, 10, theBoard)
    create_circle(200, 150, 10, theBoard)
    #spots 75-79
    create_circle(220, 160, 10, theBoard)
    create_circle(240, 170, 10, theBoard)
    create_circle(260, 180, 10, theBoard)
    create_circle(280, 190, 10, theBoard)
    create_circle(300, 200, 10, theBoard)
    #spots 80-83
    create_circle(300, 180, 10, theBoard)
    create_circle(300, 160, 10, theBoard)
    create_circle(300, 140, 10, theBoard)
    create_circle(300, 120, 10, theBoard)
    #spot 85/middle
    create_circle(340, 280, 10, theBoard)
def create_board(Board,Array):
    for x in Array:
        i = 0
        xpos = 0
        for y in x:
            if i == 0:
                xpos = y
            elif i == 1:
                ypos = y
                create_circle(xpos,y,10,theBoard)
            i = i+1
def create_coloured_board(Board,Array,Colour):
    for x in Array:
        i = 0
        xpos = 0
        for y in x:
            if i == 0:
                xpos = y
            elif i == 1:
                ypos = y
                create_coloured_circle(xpos,y,10,theBoard,Colour)
            i = i+1    
def popup_playercount(root,board):
    root.destroy()
    win = Toplevel()
    win.geometry("300x50")
    msg = Label(win, text="Number of Players: ")
    pcount = ttk.Combobox(win, values=[2,3,4,5,6 ]) 
    pcount.current(0)
    b = Button(win, text="Select", command = lambda: startGame(win,int(pcount.get()),board))


    msg.grid(row=1, column=0)
    pcount.grid(row=1, column=2)
    b.grid(row=1, column=3)
def startGame(root,pCount,board):
    root.destroy()
    x=0
    players = []
    while(x<pCount):
        players.append(player(x))
        x = x+1
        print(x)
    newTurn(players, board)
def newTurn(players, board):
    for player in players:
        roll = rollDie()
        playerMSG = Label(board, text="Player number " + player.getPlayerNumber() + " choose a piece to move: ", fg=player.colour)   
        rollMSG = Label(board, text="You Rolled a  " + str(roll))
        playerMSG.place(x=550, y = 200)
        rollMSG.place(x=550, y = 220)
   
        buttons=[]
        i = 0
        for marbles in player.marbles:
            if marbles.getPosition() == player.startPosition:
                if roll == 1 or 6:
                    print(i)
                    buttons.append( Button(board, text="Move marble "+ str(i+1), command = lambda: moveFromHome(marbles,player,board)))
                    ypos = 250 + i * 30
                    buttons[i].place(x=550, y= ypos)
                    i=i+1
            else:
                buttons.append( Button(board, text="Move marble "+ str(i+1), command = lambda: moveFromHome(marbles,player,board)))
                ypos = 250 + i * 30
                buttons[i].place(x=550, y= ypos)
                i=i+1
def moveFromHome(marbels,player,board):
    print("place Holder")
    player.marblesAtHome = player.marblesAtHome - 1
    if player.marblesAtHome == 0:
        print("stage 2")



boardArray = [[340,280],[300,100],[320,100],[340,100],[360,100],[380,100],[380,120],[380,140],[380,160],
[380,180],[380,200],[400,190],[420,180],[440,170],[460,160],[480,150],[490,170],[500,190],[510,210],[520,230],
[500,240],[480,250],[460,260],[440,270],[420,280],[440,290],[460,300],[480,310],[500,320],[520,330],[510,350],
[500,370],[490,390],[480,410],[460,400],[440,390],[420,380],[400,370],[380,360],[380,380],[380,400],[380,420],
[380,440],[380,460],[360,460],[340,460],[320,460],[300,460],[300,440],[300,420],[300,400],[300,380],[300,360],
[280,370],[260,380],[240,390],[220,400],[200,410],[190,390],[180,370],[170,350],[160,330],[180,320],[200,310],
[220,300],[240,290],[260,280],[240,270],[220,260],[200,250],[180,240],[160,230],[170,210],[180,190],[190,170],
[200,150],[220,160],[240,170],[260,180],[280,190],[300,200],[300,180],[300,160],[300,140],[300,120]] 
#home Locations

homeArray = [[410,100],[270,460],[145,305],[535,255],[215,120],[460, 450]]
window = Tk() 
window.title('Agrivation')
window.geometry("900x600")

theBoard = Canvas(window, width = 800, height = 800)
theBoard.pack()
Marbels = Canvas(theBoard, width = 800, height = 800)


# create x, horizontal y, vertical
stGameBut = Button(window, text="Start Game", command = lambda:popup_playercount(stGameBut,theBoard))
stGameBut.place(x=700,y= 300)
exitGameButton = Button(window, text="Exit", command = window.destroy)
exitGameButton.place(x=700, y = 500)
create_board(theBoard, boardArray)
create_coloured_board(theBoard,homeArray,"red")
window.mainloop()
i=0
