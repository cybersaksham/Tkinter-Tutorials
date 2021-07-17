import time
from tkinter import *


class GUI(Tk):
    def __init__(self, title):
        super().__init__()
        self.geometry("500x300")
        self.title(title)
        self.var = StringVar()
        self.var.set("Ready")
        self.statusBar = Label(self, textvariable=self.var, relief=SUNKEN, anchor="w", bg="grey", fg="white", padx=10)
        self.statusBar.pack(side=BOTTOM, fill=X)

    def status(self, statusVar):
        self.var.set(statusVar)

    def createBtn(self, text):
        Button(self, text=text, command=self.btnWork).pack()

    def btnWork(self):
        self.status("Uploading...")
        self.statusBar.update()
        time.sleep(3)
        self.status("Uploaded...")
        self.statusBar.update()
        time.sleep(3)
        self.status("Ready")
        self.statusBar.update()


if __name__ == '__main__':
    root = GUI("GUI by OOPS")
    root.createBtn("Upload")
    root.mainloop()
