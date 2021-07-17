from tkinter import *

root = Tk()
root.title("List-Box")

canvas_width = 500
canvas_height = 300

root.geometry(f"{canvas_width}x{canvas_height}")
root.minsize(canvas_width, canvas_height)
root.maxsize(canvas_width, canvas_height)


def addItem():
    global i
    lbx.insert(ACTIVE, f"Item {i}")
    i += 1


i = 1
lbx = Listbox(root)
lbx.pack()

Button(root, text="Add Item", command=addItem).pack()

root.mainloop()
