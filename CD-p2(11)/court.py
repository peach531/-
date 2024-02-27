from tkinter import *

class Court:

    def __init__(self, window,width,height,img) :

        self.canvas = Canvas(window, width = width, height = height)

        self.img = PhotoImage(file = img)
        self.canvas.create_image(width/2,height/2,image = self.img)

        self.width = width
        self.height = height

        self.canvas.pack()
