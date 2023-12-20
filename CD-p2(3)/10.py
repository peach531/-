from tkinter import *

win = Tk()

def add(event):
    lbl['text'] = int(lbl['text']) + int(entry.get())
    entry.delete(0,END)
def clear():
    lbl['text'] = 0
    
lbl = Label(win, text = "0")
btn = Button(win,text = "clear",command = clear)
entry = Entry(win)
entry.bind("<Return>", add)

lbl.pack()
entry.pack()
btn.pack()
win.mainloop()
    
