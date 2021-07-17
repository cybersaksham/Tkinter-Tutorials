from tkinter import *
import time

root = Tk()
root.title("Status Bar")

canvas_width = 500
canvas_height = 300

root.geometry(f"{canvas_width}x{canvas_height}")
root.minsize(canvas_width, canvas_height)
root.maxsize(canvas_width, canvas_height)


def upload():
    status.set("Uploading...")
    sbar.update()
    time.sleep(3)
    status.set("Uploaded...")
    sbar.update()
    time.sleep(3)
    status.set("Ready")
    sbar.update()


status = StringVar()
status.set("Ready")

sbar = Label(root, textvariable=status, relief=SUNKEN, anchor="w", bg="grey", fg="white", padx=10)
sbar.pack(side=BOTTOM, fill=X)

Button(root, text="Upload", command=upload).pack()

root.mainloop()
