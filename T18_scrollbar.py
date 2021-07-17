from tkinter import *

root = Tk()
root.title("Scroll Bar")

canvas_width = 500
canvas_height = 300

root.geometry(f"{canvas_width}x{canvas_height}")
root.minsize(canvas_width, canvas_height)
root.maxsize(canvas_width, canvas_height)

"""
For connecting vertical scrollbar to a widget :
    1. widget(yscrollcommand=scrollbar.set())
    2. scrollbar.config(command=widget.yview)
"""

scroll1 = Scrollbar(root)
scroll1.pack(side=RIGHT, fill=Y)

lbx = Listbox(root, yscrollcommand=scroll1.set)
for i in range(500):
    lbx.insert(END, f"Item {i + 1}")
lbx.pack(fill=BOTH)

scroll1.config(command=lbx.yview)

root.mainloop()
