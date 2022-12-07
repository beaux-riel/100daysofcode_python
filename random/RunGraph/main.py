# Random side project to turn my run kilometers (day 37) into a desktop app.
# Incredibly simple.
from tkinter import *
import webview

# Shows graph but none of the rollover features/insights work
window = webview.create_window('Beaux\'s Run Graph', 'https://pixe.la/v1/users/b34ux/graphs/graph1')
webview.start()