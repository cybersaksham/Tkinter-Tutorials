from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.title("Sliders")

canvas_width = 500
canvas_height = 300

root.geometry(f"{canvas_width}x{canvas_height}")
root.minsize(canvas_width, canvas_height)
root.maxsize(canvas_width, canvas_height)


def getDollars():
    tmsg.showinfo("Dollars", f"We will pay {slider_hor.get()} dollars to you.")


# Vertical Slider
slider_ver = Scale(root, from_=0, to=100)
slider_ver.pack()

# Horizontal Slider
Label(root, text="How many dollars?").pack()
slider_hor = Scale(root, from_=0, to=100, orient=HORIZONTAL)
slider_hor.set(50)
slider_hor.pack()
Button(root, text="Get", command=getDollars).pack()

root.mainloop()
