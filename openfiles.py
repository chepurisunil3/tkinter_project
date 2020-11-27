from tkinter import *
from tkinter import filedialog
import os
def openDialgoAndAdd():
    fileName = filedialog.askopenfilename(initialdir = "/",title = "Select a File",filetypes = (("executables","*.exe"),("all files","*.*")))
root = Tk()
canvas = Canvas(root,width = 700,height = 700,bg = "#263d42")
canvas.pack()
frame = Frame(root,bg = "white")
frame.place(relwidth = 0.8,relheight = 0.8,relx = 0.1,rely = 0.1)
openFile = Button(root,padx = 10,pady = 10,text = "Open File",fg = "white",bg = "#263d42",command = openDialgoAndAdd)
openFile.place(relheight = 0.1,rely = 0.1,relwidth = 0.1,relx = 0.0)
runApps = Button(root,padx = 10,pady = 10,text = "Run Apps",fg = "white",bg = "#263d42")
runApps.place(relheight = 0.1,rely = 0.2,relwidth = 0.1,relx = 0.0)
root.mainloop()