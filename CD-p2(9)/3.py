from tkinter import *   

win = Tk()
canvas = Canvas(win,bg = "white", width = 450, height = 450)
canvas.pack()

x1,y1 = 0,0
x2,y2 = 45,450
for i in range(10):
    x1 += 45
    x2 = x1
    canvas.create_line(x1,y1,x2,y2,fill = "red", width = 3)
x1,y1 = 

win.mainloop()
