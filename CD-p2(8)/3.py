from tkinter import *

def double_click(event):
    index = listbox.curselection()
    lbl1['text'] = listbox.get(index[0])
    
flower = ["rose","lily","pansy","sunflower"]
win = Tk()
lbl1 = Label(win,text = "",bg = "pink", fg = "blue")
listbox = Listbox(win)

for i in range(4):
    listbox.insert(i, flower[i])

listbox.bind("<Double-Button-1>",double_click)
lbl1.pack()
listbox.pack()
win.mainloop()

