from tkinter import *

def create_grid(event=None):
    w = c.winfo_width() # Get current width of canvas
    h = c.winfo_height() # Get current height of canvas
    # Creates all vertical lines at intevals of 100
    for i in range(0, w, 10):
        c.create_line([(i, 0), (i, h)], tag='grid_line')

    # Creates all horizontal lines at intevals of 100
    for i in range(0, h, 10):
        c.create_line([(0, i), (w, i)], tag='grid_line')
def create_circle(x, y, r, canvasName): #center coordinates, radius
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvasName.create_oval(x0, y0, x1, y1)



window = Tk() 
window.title('Agrivation')
window.geometry("800x800")

theBoard = Canvas(window, width = 800, height = 800)

theBoard.pack()
# create x, horizontal y, vertical
def create_board(theBoard):

    create_circle(300, 100, 10, theBoard)
    create_circle(320, 100, 10, theBoard)
    create_circle(340, 100, 10, theBoard)
    create_circle(360, 100, 10, theBoard)
    create_circle(380, 100, 10, theBoard)

    create_circle(380, 120, 10, theBoard)
    create_circle(380, 140, 10, theBoard)
    create_circle(380, 160, 10, theBoard)
    create_circle(380, 180, 10, theBoard)
    create_circle(380, 200, 10, theBoard)

    create_circle(400, 191, 10, theBoard)
    create_circle(420, 181, 10, theBoard)
    create_circle(440, 171, 10, theBoard)
    create_circle(460, 161, 10, theBoard)
    create_circle(480, 151, 10, theBoard)

    create_circle(280, 190, 10, theBoard)
    create_circle(260, 180, 10, theBoard)
    create_circle(240, 170, 10, theBoard)
    create_circle(220, 160, 10, theBoard)
    create_circle(200, 150, 10, theBoard)

    create_circle(190, 170, 10, theBoard)
    create_circle(180, 190, 10, theBoard)
    create_circle(170, 210, 10, theBoard)
    create_circle(160, 230, 10, theBoard)

    create_circle(180, 240, 10, theBoard)
    create_circle(200, 250, 10, theBoard)
    create_circle(220, 260, 10, theBoard)
    create_circle(240, 270, 10, theBoard)
    create_circle(260, 280, 10, theBoard)

    create_circle(240, 290, 10, theBoard)
    create_circle(220, 300, 10, theBoard)
    create_circle(200, 310, 10, theBoard)
    create_circle(180, 320, 10, theBoard)

    create_circle(490, 171, 10, theBoard)
    create_circle(500, 191, 10, theBoard)
    create_circle(510, 211, 10, theBoard)
    create_circle(520, 231, 10, theBoard)
    
    create_circle(500, 240, 10, theBoard)
    create_circle(480, 250, 10, theBoard)
    create_circle(460, 260, 10, theBoard)
    create_circle(440, 270, 10, theBoard)
    create_circle(420, 280, 10, theBoard)

    create_circle(441, 290, 10, theBoard)
    create_circle(461, 300, 10, theBoard)
    create_circle(481, 310, 10, theBoard)
    create_circle(501, 320, 10, theBoard)
    create_circle(521, 330, 10, theBoard)

    create_circle(511, 350, 10, theBoard)
    create_circle(501, 370, 10, theBoard)
    create_circle(491, 390, 10, theBoard)
    create_circle(481, 410, 10, theBoard)

    create_circle(461, 405, 10, theBoard)
    create_circle(441, 395, 10, theBoard)
    create_circle(421, 385, 10, theBoard)
    create_circle(401, 375, 10, theBoard)
    create_circle(381, 365, 10, theBoard)

    create_circle(300, 120, 10, theBoard)
    create_circle(300, 140, 10, theBoard)
    create_circle(300, 160, 10, theBoard)
    create_circle(300, 180, 10, theBoard)
    create_circle(300, 200, 10, theBoard)

    
    create_circle(320, 465, 10, theBoard)
    create_circle(340, 465, 10, theBoard)
    create_circle(360, 465, 10, theBoard)
   

    create_circle(300, 385, 10, theBoard)
    create_circle(300, 405, 10, theBoard)
    create_circle(300, 425, 10, theBoard)
    create_circle(300, 445, 10, theBoard)
    create_circle(300, 465, 10, theBoard)

    create_circle(380, 385, 10, theBoard)
    create_circle(380, 405, 10, theBoard)
    create_circle(380, 425, 10, theBoard)
    create_circle(380, 445, 10, theBoard)
    create_circle(380, 465, 10, theBoard)



    create_circle(220, 405, 10, theBoard)
    create_circle(240, 395, 10, theBoard)
    create_circle(260, 385, 10, theBoard)
    create_circle(280, 375, 10, theBoard)
    create_circle(300, 365, 10, theBoard)
    
    create_circle(160, 335, 10, theBoard)
    create_circle(170, 355, 10, theBoard)
    create_circle(180, 375, 10, theBoard)
    create_circle(190, 395, 10, theBoard)
    create_circle(200, 415, 10, theBoard)
create_board(theBoard)
window.mainloop()