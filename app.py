from tkinter import *
# from PIL import ImageTK, Image

root = Tk()
root.title('Wiki Type')
# root.iconbitmap('')

# my_img = ImageTK.PhotoImage(Image.open(''))
# img_label = Label(image=my_img)
# img_label.pack()

# Create a Label widget
Main_Label = Label(root, text="Test")
Second_Label = Label(root, text="Hey")

e = Entry(root)
e.grid(row=0, column=2)
e.insert(0, 'this is a test')


def click():
    Label(root, text=e.get()).grid(row=1, column=2)


myButton = Button(root, text='Add Text', command=click)
# Quit button
button_quit = Button(root, text='Exit', command=root.quit)

# Spacing
Main_Label.grid(row=0, column=0)
Second_Label.grid(row=1, column=0)
myButton.grid(row=2, column=1)
button_quit.grid(row=2, column=2)

root.mainloop()
