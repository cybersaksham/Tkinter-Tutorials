from tkinter import *


def getVals():
    print(nameVal.get())
    print(phoneVal.get())

    print("Gender -", end=" ")
    if genderVal.get() == 1:
        print("Male")
    elif genderVal.get() == 2:
        print("Female")

    print("Payment Mode -", end=" ")
    if paymentModeVal.get() == 1:
        print("Online")
    elif paymentModeVal.get() == 2:
        print("Offline")

    print("Prebook food -", end=" ")
    if foodServiceVal.get() == 1:
        print("Yes")
    else:
        print("No")

    nameVal.set("")
    phoneVal.set("")
    genderVal.set(0)
    paymentModeVal.set(0)
    foodServiceVal.set(0)


root = Tk()
root.title("Travel Form")

root.geometry("400x300")
root.minsize(400, 300)
root.maxsize(400, 300)

# Heading
Label(root, text="Welcome to our travels", font="comicsansms 13 bold").grid(row=0, column=3)

# Labels
name = Label(root, text="Name")
phone = Label(root, text="Phone")
gender = Label(root, text="Gender")
paymentMode = Label(root, text="Payment Mode")

# Packing labels
name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
paymentMode.grid(row=4, column=2)

# Making variables for entries
nameVal = StringVar()
phoneVal = StringVar()
genderVal = IntVar()
paymentModeVal = IntVar()
foodServiceVal = IntVar()

# Making entries
nameEntry = Entry(root, textvariable=nameVal)
phoneEntry = Entry(root, textvariable=phoneVal)
paymentModeEntry = Entry(root, textvariable=paymentModeVal)

# Packing entries
nameEntry.grid(row=1, column=3)
phoneEntry.grid(row=2, column=3)

# Packing gender
genderFrame = Frame(root)
genderFrame.grid(row=3, column=3)
Radiobutton(genderFrame, text="Male", variable=genderVal, value=1).grid(row=0, column=0)
Radiobutton(genderFrame, text="Female", variable=genderVal, value=2).grid(row=0, column=1)

# Packing payment mode
paymentFrame = Frame(root)
paymentFrame.grid(row=4, column=3)
Radiobutton(paymentFrame, text="Online", variable=paymentModeVal, value=1).grid(row=0, column=0)
Radiobutton(paymentFrame, text="Offline", variable=paymentModeVal, value=2).grid(row=0, column=1)

# Checkbox
foodService = Checkbutton(text="Want to prebook Meals?", variable=foodServiceVal)
foodService.grid(row=5, column=3)

# Submit Button
Button(text="Submit", command=getVals).grid(column=3)

root.mainloop()
