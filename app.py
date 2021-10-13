from tkinter import *
from datetime import datetime
from bs4 import BeautifulSoup
import requests
import appConfig

app = Tk()
appConfig.css(app)

url = 'https://www.naver.com'
req = requests.get(url)
soup = BeautifulSoup(req.text, 'html.parser')
txt = soup.find("div", attrs={"class", "stock_box"}).get_text()

print(txt.split('\n')[1:4])


def alert():
    if(ent.get() == '123'):
        print('일이삼입 일이삼')
    else:
        print(ent.get())
        print(ent.get())
        print(ent.get())
        print(ent.get())


ent = Entry(app)
ent.pack()


btn = Button(app)
btn.config(text="입력")
btn.config(command=alert)
btn.pack()


app.mainloop()
