from tkinter import *

root = Tk()

# Create a Label widget
myLabel1 = Label(root, text="Hello")
myLabel2 = Label(root, text="Hey")

e = Entry(root).grid(row=0, column=2)


def click():
    Label(root, text="check").grid(row=1, column=2)


myButton = Button(root, text='button', command=click)

# Spacing
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=0)
myButton.grid(row=2, column=1)


root.mainloop()
