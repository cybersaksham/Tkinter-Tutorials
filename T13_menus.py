from tkinter import *

root = Tk()
root.title("Menus & Submenus")

canvas_width = 500
canvas_height = 300

root.geometry(f"{canvas_width}x{canvas_height}")
root.minsize(canvas_width, canvas_height)
root.maxsize(canvas_width, canvas_height)


def file_func():
    print("File button clicked")


# Making non-dropdown menu
"""
myMenu = Menu(root)
myMenu.add_command(label="File", command=file_func)
myMenu.add_command(label="Exit", command=quit)
root.config(menu=myMenu)
"""

# Making a dropdown menu
myMenu2 = Menu(root)
root.config(menu=myMenu2)

m1 = Menu(myMenu2, tearoff=0)  # tearoff = 0 for removing horizontal dashed line
m1.add_command(label="New File", command=file_func)
m1.add_command(label="Save", command=file_func)
m1.add_separator()
m1.add_command(label="Print", command=file_func)
myMenu2.add_cascade(label="File", menu=m1)

m2 = Menu(myMenu2, tearoff=0)  # tearoff = 0 for removing horizontal dashed line
m2.add_command(label="Save", command=quit)
m2.add_command(label="Don't Save", command=quit)
m2.add_command(label="Exit", command=quit)
myMenu2.add_cascade(label="Exit", menu=m2)

root.mainloop()
