from tkinter import*

win = Tk()
canvas = Canvas(win,bg = "white", width = 500, height = 500)
canvas.pack()
x1,y1 = 0,0
x2,y2 = 500,0
for i in range(10):
    canvas.create_line(x1,y1,x2,y2)
    y1 += 50
    y2 = y1

x1,y1 = 0,0
x2,y2 = 0,500
for i in range(10):
    canvas.create_line(x1,y1,x2,y2)
    x1 += 50
    x2 = x1

canvas.create_polygon(100,50,100,450,400,450,fill = "red")
    
win.mainloop()

