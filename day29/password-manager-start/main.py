# Day 29 of 100 Days of Code - Python
# https://www.udemy.com/course/100-days-of-code/
# Exercise - Building a Password Manager GUI App with Tkinter

from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="day29/password-manager-start/logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.pack()

window.mainloop()