from tkinter import *

root = Tk()
root.title("Images")

image = PhotoImage(file="1.png")

"""
For jpg images

from PIL import Image, ImageTk  # pip install pillow
photo = Image.open("1.jpg")
image = ImageTk.PhotoImage(photo)
"""

img_label = Label(image=image)
img_label.pack()

root.mainloop()
