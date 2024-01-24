from tkinter import *
from datetime import datetime

class Gallery :

    def __init__(self, listbox, lbl_img, lbl_info, file_name):
        self.listbox = listbox
        self.lbl_img = lbl_img
        self.lbl_info = lbl_info
        self.file_name = file_name

        f = open(self.file_name,'r', encoding = 'UTF8')
        data = f.readlines()
        for lin in data:
            img_name = line.split(',')
            self.listbox.insert(END,img_name[0])
            f.close()
        
    def img_insert(self, text_box):

        self.data = datetime.today().strftime("%Y/%m/%d %H:%M:%S")
        f = open(self.file_name,'a',encoding = 'UTF8')
        photo_info = text_box.get('1.0',END)
        f,write("%s, %s\n" % (photo_info[:-1],self.date))
        title = photo_info.split(',')
        self.listbox.insert(END,title[0])
        f.close()
        text_box.delete('1.0',END)

win = Tk()
win.title("나만의 사진첩")

img = PhotoImage(file = "basic.png")

img_lbl = Label(win,image = img, width = 500, height = 300,relief = "solid")
info_lbl = Label(win,text = "파일명과 메모를 \n쉼표(,)로 구분지어 작성한 후\n save 버튼을 클릭하세요",
                 width = 40,bg = "yellow",fg = "red")

img_list = Listbox(win, height = 20, width = 50)
text_box = Text(win, height = 15, width = 30)
save_btn = Button(win, text = "save", bg = "yellow",fg = "red",
                  command = lambda: setImg.img_insert(text_box))

img_lbl.grid(row = 0, column = 0)
info_lbl.grid(row = 1,column = 0, columnspan = 3)
guide_lbl.grid(row = 1, column = 1, columnspan = 2)
img_list.grid(row = 0, column = 1, columnspan = 2)
text_box.grid(row = 2, column = 1)
save_btn.grid(row = 2, column = 2f

file_name




gallery = Gallery(img_list, img_lbl, file_name)

win.mainloop()
