from tkinter import *
from functools import partial
from tkinter import messagebox
import os
from functools import partial


def load_CallBack(func_input) :
    print("Load")


def open_CallBack(func_input) :
    print("Open")


def start_CallBack(func_input) :
    print("Start")


def refresh_CallBack(func_input) :
    print("Refreshed")


def close_CallBack(page) :
    print("Close")
    page.withdraw()
    os._exit(0)

# Main Page
root = Tk()
root.title("Detection")
root.geometry("1200x800")

 # Frames
top_frame = Frame(root, bg='#282828', bd=2)
top_frame.pack(side=TOP, fill=X)

center_Canvas = Canvas(root, height=800, width=1200, bg="#282828")
center_Canvas.pack()

center_frame = Frame(center_Canvas, bg="white")
center_frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

func_input = "You can use for anything" # You can use it command = partial(function,input,input)

# Buttons
load_Button = Button(top_frame, text="Load", command=partial(load_CallBack,func_input), compound=TOP)
load_Button.pack(side=LEFT)


open_Button = Button(top_frame, text="Open", command=partial(open_CallBack,func_input), compound=TOP)
open_Button.pack(side=LEFT)

start_Button = Button(top_frame, text="Start", command=partial(start_CallBack,func_input), compound=TOP)
start_Button.pack(side=LEFT)


exit_Button = Button(top_frame, text="Exit", command=partial(close_CallBack,root), compound=TOP)
exit_Button.pack(side=RIGHT)

refresh_Button = Button(top_frame, text="Refresh", command=partial(refresh_CallBack,func_input), compound=TOP)
refresh_Button.pack(side=RIGHT)

info = "Welcome"
info_label = Label(center_frame,text = info, anchor = CENTER)
info_label.config(font=("Courier", 24))
info_label.pack(side = TOP)


info2 = "How to use"
info2_label = Label(center_frame,text = info2, anchor = CENTER)
info2_label.config(font=("Courier", 12))
info2_label.pack(side = TOP)


devs = "Developers:"
devs_label = Label(center_frame,text = devs)
devs_label.config(font=("Ariel", 18))
devs_label.pack()


devs2 = "Doğukan Duduloğlu, Kerem Güre, Cenker Karaörs, Ertuğrul Özvardar"
devs2_label = Label(center_frame,text = devs2)
devs2_label.config(font=("Ariel", 12))
devs2_label.pack()


root.resizable(True,True)
root.mainloop()