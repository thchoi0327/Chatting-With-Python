from tkinter import *
import requests
from bs4 import BeautifulSoup

win = Tk()
win.title("Naver Log-in")
x = 400
y = 300
widthX = (win.winfo_screenwidth() - x)/2
heightY = (win.winfo_screenheight() - y)/2
win.geometry('%dx%d+%d+%d' % (x, y, widthX, heightY))
win.option_add("*Font", "궁서 20")


# id 라벨
lab1 = Label(win)
lab1.config(text="id")
lab1.pack()
# id 입력창
ent1 = Entry(win)

ent1.pack()

# pw 라벨
lab2 = Label(win)
lab2.config(text="password")
lab2.pack()


# pw 입력창
ent2 = Entry(win)
ent2.config(show="*")
ent2.pack()


def ChattingLogin():
    url = "http://192.168.0.57:8181/huefax/H_fbComment.do?cmd=ChattingLogin"
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")
    print(soup)


# 로그인 버튼
btn = Button(win)
btn.config(text="로그인")
btn.config(command=ChattingLogin)
btn.pack()
win.mainloop()
