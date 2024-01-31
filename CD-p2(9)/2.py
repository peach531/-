from tkinter import *

win = Tk()
canvas = Canvas(win,bg = "white", width = 500, height = 500)
canvas.create_line(250,100,250,400,fill = "red", width = 5)
canvas.pack()
win.mainloop()
