from tkinter import *

win = Tk()
img = PhotoImage(file = 'pizza.png')
lbl = Label(win, image = img)
lbl.pack()
win.mainloop()
