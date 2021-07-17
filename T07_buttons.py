from tkinter import *

root = Tk()
root.title("Buttons")
root.geometry("700x700")


def func1():
    print("This is function 1")


def func2():
    print("This is function 2")


b1 = Button(fg="red", text="Button 1", command=func1)
b1.pack()

b2 = Button(fg="red", text="Button 2", command=func2)
b2.pack()

root.mainloop()
