from tkinter import *


def apply():
    try:
        root.geometry(f"{width.get()}x{height.get()}")
        status.config(text="Geometry changed!!!")
    except Exception as e:
        status.config(text="Incorrect values!!!")
    finally:
        width.set("")
        height.set("")


root = Tk()
root.title("Resizing")

canvas_width = 500
canvas_height = 300

root.geometry(f"{canvas_width}x{canvas_height}")

Label(root, text="Height").grid(row=0, column=0)
Label(root, text="Width").grid(row=1, column=0)

height = StringVar()
width = StringVar()

Entry(root, textvariable=height).grid(row=0, column=1)
Entry(root, textvariable=width).grid(row=1, column=1)

Button(text="Apply", command=apply).grid(row=2, column=1)
status = Label(text="")
status.grid(row=3, column=1)

root.mainloop()
