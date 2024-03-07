from tkinter import *

count = 0

def btn_click():
    global count
    count = count + 2
    btn.config(text=count)


window = Tk()
btn = Button(window, text="Click me!",
command=btn_click)


btn.pack()

window.mainloop()
