from tkinter import *
from random import *

def draw_shape(event):
    color = ["black","white","blue","red","green","yellow"]
    x1,y1 = event.x,event.y
    canvas.create_oval(x1-25,y1,x1+25,y1+50,fill = color[randint(0,5)])

win = Tk()
canvas = Canvas(win, width = 300, height = 300,bg = "white")
canvas.pack()

canvas.bind("<Double-Button-1>", draw_shape)

win.mainloop()
