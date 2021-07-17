from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.title("Radio Buttons")

canvas_width = 500
canvas_height = 300

root.geometry(f"{canvas_width}x{canvas_height}")
root.minsize(canvas_width, canvas_height)
root.maxsize(canvas_width, canvas_height)


def order():
    tmsg.showinfo("Your Order", f"You ordered {foodList[var.get() - 1]}")
    var.set(0)


var = IntVar()
Label(root, text="What would you like to have").pack()
foodList = [f"Item {i + 1}" for i in range(5)]
for i in range(len(foodList)):
    radio = Radiobutton(root, text=foodList[i], variable=var, value=(i + 1)).pack()

Button(root, text="Order Now", command=order).pack()

root.mainloop()
