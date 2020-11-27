from tkinter import *

def onClick():
    myLabel.config(text = inp.get())
root = Tk()
root.title("Calculator")
inp = Entry(root,width = 35, fg = "black", bg = "white", borderwidth = 5)
inp.grid(row=0,column=0,columnspan=3,padx = 5,pady = 5)
btn_1 = Button(root,text = "1",command = onClick,padx = 50, pady = 50)
btn_1.grid(row = 1,column = 0)
btn_2 = Button(root,text = "2",command = onClick,padx = 50, pady = 50)
btn_2.grid(row = 1,column = 1)
btn_3 = Button(root,text = "3",command = onClick,padx = 50, pady = 50)
btn_3.grid(row = 1,column = 2)
root.mainloop()