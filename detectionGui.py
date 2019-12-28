# Authors: Kerem Güre, Cenker Karaörs, Ertuğrul Özvardar, Doğukan Duduoğlu

from tkinter import *
from functools import partial
from tkinter import messagebox
import os
from functools import partial
import cv2
from PIL import Image
import importlib
import numpy as np
import threading

# https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/detection_model_zoo.md
model_to_use = 'ssd_mobilenet_v1_coco_2017_11_17' # Default model

tensorActive = False
capture_device = None
cameraThread = None
tensor_run = None
captured_frame = None
camera_open = False
model_loaded = False # Some global statements to control the flow of the program.

root = None # Tkinter root Frame

def notification(message:str):
    # Get the w,h of the root Frame to calculate and place the notification centered.
    windowWidth = root.winfo_reqwidth()
    windowHeight = root.winfo_reqheight() 
    # print("Width",windowWidth,"Height",windowHeight)

    # Gets both half the screen width/height and window width/height
    positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2)
    positionDown = int(root.winfo_screenheight()/2 - windowHeight/2)

    # Position the notification in the center of the root Frame.
    notification = Toplevel(master=root,height=3,width=10) # Toplevel widget of tkinter
    notification.geometry("+{}+{}".format(positionRight, positionDown))
    notification.wm_attributes("-topmost",True) # set this flag to have always-on-top effect.
    notification.overrideredirect(1)
    notification.withdraw() # this removes all the defaults on the widget
    lb = Label(notification,text=message,foreground="white",background="#282828",height=3,font=("Roboto",16)) # set the message
    lb.pack()
    notification.deiconify() # removes all the icons and window framings.
    notification.tkraise() # show it
    return notification

def load_helper(note : Toplevel):
    global tensor_run
    tensor_run = importlib.import_module('.','tensor_run') # using importlib to dynamically load the tensor_run to decrease program loading time
    tensor_run.load_model(model_to_use) # load the model
    note.withdraw() # purge the notification
    print("here")
    return
    

def load_model_btn_callback():
    global model_loaded
    model_loaded = True
    note = notification("Tensorflow is loading...") # create new notification
    print("Loading")
    # time.sleep(2)
    th = threading.Thread(target=load_helper,args=[note]) # spawn new thread
    th.start() #start the thread
    return th
    # note.withdraw()

def camera_helper():
    global captured_frame
    while capture_device.isOpened(): # wait untill the camera is ready
        ret, captured_frame = capture_device.read() # capture a frame
        # allows us to close the camera using the X on the window or 'q' on keyboard.
        if cv2.waitKey(1) & 0xFF == ord('q') or cv2.getWindowProperty('image',cv2.WND_PROP_VISIBLE) < 1:
            global camera_open
            camera_open = False
            break
        if not tensorActive:
            cv2.imshow('image',captured_frame) # if tensorflow not active show normal feed.
        else:
            cv2.imshow('image',tensor_run.show_inference(captured_frame)) # tensorflow active process and show.
        
    cv2.destroyWindow('image')
    capture_device.release()
    return

def open_camera_btn_callback():
    print("Open")
    global camera_open
    camera_open = True
    global capture_device
    capture_device = cv2.VideoCapture(0) # open the default capture device
    cv2.namedWindow('image', cv2.WINDOW_NORMAL) # create new window
    global cameraThread
    cameraThread = threading.Thread(target=camera_helper) # start the camera driver thread
    cameraThread.start()
    return cameraThread
    


def start_model_btn_callback():
    print("Start")
    if not (model_loaded or camera_open):
        note = notification("Please load the model and open the camera first!")
        note.after(3000,(lambda: note.withdraw()))
    else:
        global tensorActive
        tensorActive = True
    

def exit_btn_callback(page):
    print("Close")
    page.withdraw() # close the gui
    if camera_open:
        capture_device.release() # close the camera feed
    cv2.destroyAllWindows() # destroy camera window
    os._exit(0) # exit


# Main Page
root = Tk()
root.title("Detection")
root.geometry("{}x{}".format(root.winfo_screenwidth(),root.winfo_screenheight()))

 # Frames
top_frame = Frame(root, bg='#282828', bd=2)
top_frame.pack(side=TOP, fill=X)

center_Canvas = Canvas(root,bg="#282828")
center_Canvas.pack(fill="both",expand=True)

center_frame = Frame(center_Canvas, bg="white")
center_frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)


# Buttons
load_Button = Button(top_frame, text="Load the Model", command=load_model_btn_callback, compound=TOP)
load_Button.pack(side=LEFT)


open_Button = Button(top_frame, text="Open Camera", command=open_camera_btn_callback, compound=TOP)
open_Button.pack(side=LEFT)

start_Button = Button(top_frame, text="Start Tensorflow", command=start_model_btn_callback, compound=TOP)
start_Button.pack(side=LEFT)


exit_Button = Button(top_frame, text="Exit", command=partial(exit_btn_callback,root), compound=TOP)
exit_Button.pack(side=RIGHT)

info_label = Label(center_frame,text = "EE393 Term Project | Object Detection\n\n", anchor = CENTER)
info_label.config(font=("Roboto", 32),fg="black",bg="white")
info_label.pack(side = TOP)


devs_label = Label(center_frame,text = "Developers:\n")
devs_label.config(font=("Ariel", 18),bg="white")
devs_label.pack()


devs2 = "Kerem Güre, Doğukan Duduoğlu\n\n Cenker Karaörs, Ertuğrul Özvardar"
devs2_label = Label(center_frame,text = devs2)
devs2_label.config(font=("Ariel", 12),bg="white",fg="red")
devs2_label.pack()


root.resizable(True,True)
root.mainloop() # gui loop