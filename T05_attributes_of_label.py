from tkinter import *

root = Tk()
root.title("Attributes of Label")
root.geometry("700x700")

"""
Important Label Attributes :
text - adds the text
bg - background
fg - foreground
font - sets the font
    1. font=("comicsansms", 19, "bold")
    2. font="comicsansms 19 bold"
padx - x padding
pady - y padding
relief - border styling - SUNKEN, RAISED, GROOVE, RIDGE
"""

title_label = Label(text="Hello, this is dummy text for our GUI.", bg="red", fg="white", padx=100, pady=100,
                    font="comicsansms 19 bold", relief=SUNKEN)

"""
Important Pack Attributes :
side - TOP, BOTTOM, LEFT, RIGHT
anchor - sets direction
    1. nw - North-West
    2. ne - North-East
    3. sw - South-West
    4. se - South-East
    
    For using sw or se we have to set side as BOTTOM
fill - fill in X or Y direction
    For using Y we have to set side as LEFT or RIGHT
padx - x padding
pady - y padding
"""

# title_label.pack(side=BOTTOM, anchor="sw")
# title_label.pack(fill=X)
title_label.pack(side=LEFT, fill=Y, padx=34, pady=34)

root.mainloop()
