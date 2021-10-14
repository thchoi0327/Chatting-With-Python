from tkinter import *
import appConfig
import requests
import json
import MainChatting

def Start():
    win = Tk();
    appConfig.loginCSS(win);


    # id 라벨
    lab1 = Label(win)
    lab1.config(text="ID")
    lab1.place(x=50,y=35)
    # id 입력창
    ent1 = Entry(win)
    ent1.place(x=125,y=35)

    # pw 라벨
    lab2 = Label(win)
    lab2.config(text="Password")
    lab2.place(x=20,y=65)

    # pw 입력창
    ent2 = Entry(win)
    ent2.config(show="*")
    ent2.place(x=125,y=65)

    # 로그인 버튼        
    btn = Button(win)
    btn.config(text="로그인")
    def ChattingLogin():
        url = "http://192.168.0.57:8181/huefax/Chatting.do?cmd=ChattingLogin"
        loginData = {'userId': ent1.get(), 'userPw': ent2.get()}
        try:
            req = requests.post(url, data=loginData)
        except requests.exceptions.RequestException as e:
            lab3.config(bg='#f3f3f3', fg='#f00');
            lab3.config(text="[메시지] 서버연결실패")
            return

        JSONdata = json.loads(str(req.text))
        data = JSONdata['result']
        if (data == 'SUCCESS'):
            lab3.config(text='[메시지] 로그인 성공')
            win.destroy();
            MainChatting.Access();
        else:
            lab3.config(text='[메시지] 로그인 실패')

    btn.config(command=ChattingLogin)
    btn.pack(side=BOTTOM,pady=10)

    # 메시지 라벨
    lab3 = Label(win)
    lab3.pack(pady=5)


    win.mainloop()


Start();








