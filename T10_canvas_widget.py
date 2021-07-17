from tkinter import *

root = Tk()
root.title("Canvas Widget")

canvas_width = 500
canvas_height = 300

root.geometry(f"{canvas_width}x{canvas_height}")
root.minsize(canvas_width, canvas_height)
root.maxsize(canvas_width, canvas_height)

can_widget = Canvas(root, width=canvas_width, height=canvas_height)
can_widget.pack()

# The line goes from (x1, y1) to (x2, y2)
can_widget.create_line(0, 10, 500, 10)
can_widget.create_line(0, 20, 500, 20, fill="red")

# Top right corner is (x1, y1) & bottom right corner is (x2, y2)
can_widget.create_rectangle(10, 30, 490, 50)
can_widget.create_rectangle(10, 60, 490, 80, fill="green")

# Center of text is (x1, y1)
can_widget.create_text(50, 90, text="This is a text")

# Top right corner is (x1, y1) & bottom right corner is (x2, y2) - Inside this rectangle oval is formed
can_widget.create_oval(10, 100, 490, 150)

root.mainloop()
