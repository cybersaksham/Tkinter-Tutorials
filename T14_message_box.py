from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.title("Message Box")

canvas_width = 500
canvas_height = 300

root.geometry(f"{canvas_width}x{canvas_height}")
root.minsize(canvas_width, canvas_height)
root.maxsize(canvas_width, canvas_height)


def file_func():
    print("File button clicked")


def help():
    a = tmsg.showinfo("Help", "I will definitely help you.")


def rate():
    rating = tmsg.askquestion("Rate Us", "Was your experience good?")
    if rating == "yes":
        msg = "Great! Please rate on playstore."
    else:
        msg = "We will resolve the problem soon."
    tmsg.showinfo("Experience", msg)


def update():
    ans = tmsg.askyesno("Update", "Do you want to update GUI?")
    if ans:
        msg = "Great! We are updating soon."
    else:
        msg = "We will stop updating process."
    tmsg.showinfo("Result", msg)


mainMenu = Menu(root)
root.config(menu=mainMenu)

m1 = Menu(mainMenu, tearoff=0)
m1.add_command(label="New File", command=file_func)
m1.add_command(label="Save", command=file_func)
m1.add_separator()
m1.add_command(label="Print", command=file_func)
mainMenu.add_cascade(label="File", menu=m1)

m2 = Menu(mainMenu, tearoff=0)
m2.add_command(label="Save", command=quit)
m2.add_command(label="Don't Save", command=quit)
m2.add_command(label="Exit", command=quit)
mainMenu.add_cascade(label="Exit", menu=m2)

m3 = Menu(mainMenu, tearoff=0)
m3.add_command(label="Help", command=help)
m3.add_command(label="Rate Us", command=rate)
m3.add_command(label="Update", command=update)
mainMenu.add_cascade(label="More", menu=m3)

root.mainloop()
