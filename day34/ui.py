from tkinter import *

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Squiggly Quizzley")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.window.mainloop()

