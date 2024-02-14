from tkinter import *

pen_color = "black"
def paint(event):
    global pen_color
    x1,y1 = event.x,event.y
    x2,y2 = x1 + 5, y1 + 5
    canvas.create_line(x1,y1,x2,y2, width = 3, fill = pen_color)
    
def change_color():
    global pen_color
    pen_color = "red"

win = Tk()
canvas = Canvas(win,bg = "white", width = 500, height = 200)
btn = Button(win,text = "red", command = change_color)

canvas.pack()
btn.pack()
win.bind("<B1-Motion>", paint)

win.mainloop()
