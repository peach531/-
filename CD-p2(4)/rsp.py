from tkinter import *
from random import *

win = Tk()

win.title("Rock paper Scissors Game")

def game(com,user):
    if user == 0:
        if com == 0: lbl_res['text'] = "Draw"
        elif com == 1 : lbl_res['text'] = "Computer wins!"
        else: lbl_res['text'] = "User wins!"
    elif user == 1:
        if com == 0: lbl_res['text'] = "User wins!"
        elif com == 1: lbl_res['text'] = "Draw"
        else : lbl_res['text'] = "Computer wins!"
    else :
        if com == 0 : lbl_res['text'] = "Computer wins!"
        elif com == 1: lbl_res['text'] = "User wins!"
        else : lbl_res['text'] = "Draw"
def change_img(user):
    List = ["scissors.png","rock.png","paper.png"]

    com = randint(0,2)

    com_img = PhotoImage(file = List[com])
    user_img = PhotoImage(file = List[user])

    lbl_com['image'] = com_img
    lbl_com.image = com_img
    lbl_user['image'] = user_img
    lbl_user.image = user_img
    
    game(com,user)
    
basic_img = PhotoImage(file = "ready.png")

lbl_com = Label(win , image = basic_img, relief = "solid")
lbl_user = Label(win , image = basic_img, relief = "solid")

lbl_res = Label(win, text = '',width = 15,font = ("consolas",20,"bold"),fg = "brown",bg = "lightyellow")

lbl_name1 = Label(win, text = "Computer", font = ("consolas",20))
                  
lbl_name2 = Label(win, text = "User", font = ("consolas",20))

btn_scissor = Button(win, text = "scissors", width = 15, font = ("consolas",15),bg = "skyblue",command = lambda : change_img(0))
btn_rock = Button(win, text = "rock", width = 15, font = ("consolas",15),bg = "pink",command = lambda : change_img(1))
btn_paper = Button(win, text = "paper", width = 15, font = ("consolas",15),bg = "light green",command = lambda : change_img(2))

lbl_com.grid(row = 0, column = 0)
lbl_res.grid(row = 0, column = 1)
lbl_user.grid(row = 0, column = 2)
lbl_name1.grid(row = 2, column = 0)
lbl_name2.grid(row = 2, column = 2)
btn_scissor.grid(row = 2, column = 0)
btn_rock.grid(row = 2, column = 1)
btn_paper.grid(row = 2, column = 2)

win.mainloop()
