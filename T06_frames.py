from tkinter import *

root = Tk()
root.title("Frames")

root.geometry("600x600")

f1 = Frame(root, bg="grey", borderwidth=3, relief=SUNKEN)
f1.pack(fill=X)

l1 = Label(f1, text="This is frame 1")
l1.pack()

f2 = Frame(root, bg="grey", borderwidth=3, relief=SUNKEN)
f2.pack(side=LEFT, fill=Y)

l2 = Label(f2, text="This is frame 2")
l2.pack(pady=100)

root.mainloop()
