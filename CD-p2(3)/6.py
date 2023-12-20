from tkinter import *

win = Tk()
img = PhotoImage(file = 'pizza.png')
lbl = Label(win, image = img)
lbl2 = Label(win, text = "Pizza", bg = "yellow",fg = "red")
lbl.pack()
lbl2.pack()
win.mainloop()
