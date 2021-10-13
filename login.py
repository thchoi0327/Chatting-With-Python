from tkinter import *
import requests
from bs4 import BeautifulSoup

win = Tk()
win.title("Naver Log-in")
win.geometry("400x300")
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
    url = "http://localhost:8181/huefax/H_fbComment.do?cmd=ChattingLogin"
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")
    print(soup)
    print(soup)
    print(soup)
    print(soup)
    print(soup)
    print(soup)
    print(soup)
    print(soup)
    print(soup)
    print(soup)
    print(soup)
    print(soup)
    print(soup)
    print(soup)


# 로그인 버튼
btn = Button(win)
btn.config(text="로그인")
btn.config(command=ChattingLogin)
btn.pack()
win.mainloop()
