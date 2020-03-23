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

create_circle(500, 191, 10, theBoard)
create_circle(520, 181, 10, theBoard)
create_circle(540, 171, 10, theBoard)
create_circle(560, 161, 10, theBoard)
create_circle(580, 151, 10, theBoard)

create_circle(300, 120, 10, theBoard)
create_circle(300, 140, 10, theBoard)
create_circle(300, 160, 10, theBoard)
create_circle(300, 180, 10, theBoard)
create_circle(300, 200, 10, theBoard)

create_circle(300, 600, 10, theBoard)
create_circle(320, 600, 10, theBoard)
create_circle(340, 600, 10, theBoard)
create_circle(360, 600, 10, theBoard)
create_circle(380, 600, 10, theBoard)

create_circle(300, 500, 10, theBoard)
create_circle(300, 520, 10, theBoard)
create_circle(300, 540, 10, theBoard)
create_circle(300, 560, 10, theBoard)
create_circle(300, 580, 10, theBoard)

create_circle(380, 500, 10, theBoard)
create_circle(380, 520, 10, theBoard)
create_circle(380, 540, 10, theBoard)
create_circle(380, 560, 10, theBoard)
create_circle(380, 580, 10, theBoard)

create_circle(400, 511, 10, theBoard)
create_circle(420, 521, 10, theBoard)
create_circle(440, 531, 10, theBoard)
create_circle(460, 541, 10, theBoard)
create_circle(480, 551, 10, theBoard)

create_circle(300, 551, 10, theBoard)
create_circle(320, 541, 10, theBoard)
create_circle(340, 531, 10, theBoard)
create_circle(360, 521, 10, theBoard)
create_circle(380, 511, 10, theBoard)
window.mainloop()