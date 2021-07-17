from tkinter import *


def click(event):
    print(f"Clicked at {event.x}, {event.y}")


root = Tk()
root.title("Events")

canvas_width = 500
canvas_height = 300

root.geometry(f"{canvas_width}x{canvas_height}")
root.minsize(canvas_width, canvas_height)
root.maxsize(canvas_width, canvas_height)

widget = Button(root, text="Click")
widget.pack()

widget.bind('<Button-1>', click)  # Clicking
widget.bind('<Double-1>', quit)  # Double click

root.mainloop()
