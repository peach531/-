from tkinter import *

win = Tk()
def click():
    if txt['text'] == "hello":
        txt['text'] = "python"
        txt['bg'] = "green"   
    else:
        txt['text'] = "hello"
        txt['bg'] = "orange"

btn = Button(win, text = "Button",command = click)
txt = Label(win, text = "hello", fg = "black", bg = "yellow")
btn.pack()
txt.pack()
win.mainloop()
