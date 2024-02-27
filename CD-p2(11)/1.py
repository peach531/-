from tkinter import *
w, h =745, 374
win = Tk()
canvas = Canvas(win, width = w, height = h)
img = PhotoImage(file = "court.png")
canvas.create_image(w/2, h/2, image = img)
canvas.pack()
win.mainloop
