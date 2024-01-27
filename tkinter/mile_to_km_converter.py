from tkinter import *

window = Tk()
window.title("Mile to Km Conveter")
window.config(padx=100, pady=100)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

miles_entry = Entry()
miles_entry.config(width=7)
miles_entry.grid(column=1, row=0)

output_label = Label(text="0")
output_label.grid(column=1, row=1)

def calculate():
    miles = float(miles_entry.get())
    km = round(1.609344 * miles, 2)
    output_label.config(text=f"{km}")
    

calculate_btn = Button(text="Calculate", command=calculate)
calculate_btn.grid(column=1, row=2)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

window.mainloop()