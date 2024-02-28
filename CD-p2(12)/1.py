from tkinter import *

def change_color(event):
    canvas.itemconfigure(board,text = "Python")

my_font = ("consolas", 20)

win = Tk()
win.title("tennis Game")
canvas = Canvas(win, width = 200, height = 100, bg = "white")

board = canvas.create_text(100,50,font = my_font, fill = "green", text = "hello")
canvas.pack()

win.bind("<Button-1>", change_color)

win.mainloop()
