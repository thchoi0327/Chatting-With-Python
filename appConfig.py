from tkinter import *

def loginCSS(win):
    win.title("huefax Log-in")
    w = 400
    h = 150
    x = (win.winfo_screenwidth() - w)/2;
    y = (win.winfo_screenheight() - h)/2;
    win.geometry('%dx%d+%d+%d' % (w, h, x, y));
    win.option_add("*Font", "고딕 15");
    win.resizable(False, False);
    return;
    
def mainCSS(app):
    app.title("huefax Log-in")
    w = 600
    h = 1000
    x = (app.winfo_screenwidth() - w)/2
    y = (app.winfo_screenheight() - h)/2
    app.geometry('%dx%d+%d+%d' % (w, h, x, y))
    app.option_add("*Font", "고딕 15")
    app.resizable(False, False)
    return;
    