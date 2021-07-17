from tkinter import *

root = Tk()
root.title("Labels")
root.geometry("500x600")

if __name__ == '__main__':
    hello = Label(text="Hello this is a GUI")
    hello.pack()
    root.mainloop()
