from tkinter import *

root = Tk()
root.title('Wiki Type')

# Create a Label widget
mainLabel = Label(root, text="Hello")
Second_Label = Label(root, text="Hey")

e = Entry(root)
e.grid(row=0, column=2)
e.insert(0, 'this is a test')


def click():
    Label(root, text=e.get()).grid(row=1, column=2)


myButton = Button(root, text='button', command=click)
# Quit button
button_quit = Button(root, text='Exit', command=root.quit)

# Spacing
mainLabel.grid(row=0, column=0)
Second_Label.grid(row=1, column=0)
myButton.grid(row=2, column=1)
button_quit.grid(row=2, column=2)

root.mainloop()
