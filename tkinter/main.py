# Tkinter
# Graphical
# User
# Interface

from tkinter import *

window = Tk()
window.title("My GUI program")
window.minsize(width=500, height=300)


my_label = Label(text="Hello I'm ", font=("Courier", 24, "normal"))
# my_label.pack() # pack to show off in tkinter
my_label.grid(column=0, row=0)

my_label["text"] = "New Text"
my_label.config(text="New Text")

def btn_clicked():
    print("I got clicked.")
    input_response = input.get()
    my_label.config(text=input_response)

btn = Button(text="Click Me", command=btn_clicked)
# btn.pack()
btn.grid(column=1, row=1)

# Input
input = Entry(width=10)
# input.pack()
input.grid(column=3, row=2)

new_btn = Button(text="Another Button")
new_btn.grid(column=2, row=0)

window.mainloop() # very end of the program
