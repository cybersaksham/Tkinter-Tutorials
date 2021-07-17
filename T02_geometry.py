from tkinter import *

root = Tk()
root.title("Geometry")

# Width x Height
root.geometry("500x600")  # Initial Geometry

# Width, Height
root.minsize(100, 100)  # Minimum Size

# Width, Height
root.maxsize(700, 700)  # Maximum Size

if __name__ == '__main__':
    root.mainloop()
