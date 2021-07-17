from tkinter import *


def getVals():
    print(userValue.get())
    print(passValue.get())


root = Tk()
root.title("Grid & Entry")
root.geometry("400x300")
root.minsize(400, 300)
root.maxsize(400, 300)

user = Label(text="Username")
password = Label(text="Password")
user.grid()
password.grid(row=1)

"""
There are 4 variable classes in tkinter :
BooleanVar, DoubleVar, IntVar, StringVar
"""

userValue = StringVar()
passValue = StringVar()

userEntry = Entry(root, textvariable=userValue)
passEntry = Entry(root, textvariable=passValue)

userEntry.grid(row=0, column=1)
passEntry.grid(row=1, column=1)

Button(text="Submit", command=getVals).grid(row=2, column=1)

root.mainloop()
