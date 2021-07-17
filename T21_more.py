from tkinter import *

root = Tk()
root.title("More Functions")

canvas_width = 500
canvas_height = 300

root.geometry(f"{canvas_width}x{canvas_height}")
root.minsize(canvas_width, canvas_height)
root.maxsize(canvas_width, canvas_height)

# Changing icon
root.wm_iconbitmap("notepad.ico")

# Configure
root.configure(background="grey")

# Height & Width
print(root.winfo_screenwidth(), "x", root.winfo_screenmmheight())

# Destroy
Button(text="Close",command=root.destroy).pack()

root.mainloop()
