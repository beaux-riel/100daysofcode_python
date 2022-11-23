# Day 27 of 100 Days of Code - Python
# https://www.udemy.com/course/100-days-of-code/
# Exercise - Tkinter, *args, **kwargs and Creating GUI Programs - Main

from tkinter import *
import time

window = Tk()
window.title("My first Gooey Program")
window.minsize(width=500, height=300)

#Label
my_label = Label(text="Do you Kardio?", font=("Arial", 24, "bold"), fg="#00A300")
my_label.pack()

# my_label["text"] = "New Text 1"
# my_label.config(text="New Text 2")

# Button

def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)

    # return my_label

button = Button(text="Repeat after me.", command=button_clicked)
button.pack()

# Entry

input = Entry(width=10)
input.pack()
input.get()

# Should always be at the end of a program
window.mainloop()