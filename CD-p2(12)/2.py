from tkinter import *

def move_up(event) :
    global x,y
    y -= 5
    canvas.coords(racket,x,y)

def move_down(event) :
    global x,y
    y += 5
    canvas.coords(racket,x,y)

def move_left(event) :
    global x,y
    x -= 5
    canvas.coords(racket,x,y)

def move_right(event) :
    global x,y
    x += 5
    canvas.coords(racket,x,y)

x,y = 400, 235

win = Tk()
canvas = Canvas(win,width = 500,height = 500, bg = "white")

img = PhotoImage(file = "red_racket.png")
racket = canvas.create_image(x,y,image = img)
canvas.pack()

win.bind("<Up>",move_up)
win.bind("<Down>",move_down)
win.bind("<Left>",move_left)
win.bind("<Right>",move_right)

win.mainloop()
