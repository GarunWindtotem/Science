# from tkinter import *

# root = Tk()
# root.title("Simple Calculator")

# e = Entry(root, width=35, borderwidth=5)
# e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
# e.insert(0, "Enter your name: ")

# def myClick():
#     hello = "Hello " + e.get()
#     myLabel = Label(root, text=hello)
#     myLabel.pack()

# myButton = Button(root, text="Enter Your Stock Quote", command=myClick)

# root.mainloop()


import PySimpleGUI as sg

sg.theme('Dark')