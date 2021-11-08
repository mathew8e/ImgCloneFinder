from tkinter import *
from tkinter import ttk
from main import *


# constants
WinName = "imgCloneFinder"



# tkinter code

win = Tk();
frm = ttk.Frame(win, padding=10)
win.title(WinName)
frm.grid();



def start():
    winpath = e1.get()
    path = winpath.replace("\\","//")+"/"
    imgs = loadImages(path)
    npimgs = convImgToNpArrays(imgs)
    cloneListArray = cloneFind(npimgs, imgs)
    deleteCloneImages(cloneListArray)

ttk.Label(frm, text="Insert path").grid(column=0, row=0, padx=10, pady=10)
e1 = Entry(frm,width=50)
e1.grid(column=1,row=0, padx=10, pady=10)
ttk.Button(frm, text="Start", command=start).grid(column=0, row=1, padx=10, pady=10)


win.mainloop();