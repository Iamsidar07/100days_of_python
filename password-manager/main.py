import json
import random
from tkinter import *
from tkinter import messagebox

import pyperclip


# Generate password
def generate_password():
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
               "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P",
               "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
               ]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)
    letters_list = [random.choice(letters) for _ in range(nr_letters)]
    symbols_list = [random.choice(symbols) for _ in range(nr_symbols)]
    numbers_list = [random.choice(numbers) for _ in range(nr_numbers)]
    password_list = letters_list + symbols_list + numbers_list
    random.shuffle(password_list)
    password = "".join(password_list)
    pyperclip.copy(password)
    password_input.insert(0, password)


def write_data(data):
    with open("data.json", mode="w") as file:
        # write data
        json.dump(data, file, indent=4)


def save_password():
    website = website_input.get()
    email = email_or_username_input.get()
    password = password_input.get()
    new_data = {website.lower(): {"email": email, "password": password}}

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showinfo(title="Oops", message="Please don't left any field empty!")
        return

    is_ok = messagebox.askokcancel(
        title=website,
        message=f"These are the details entered:\nEmail: {email}\nPassword: {password}",
    )
    if is_ok:
        try:
            with open("data.json", mode="r") as file:
                # read data
                data = json.load(file)
        except FileNotFoundError:
            write_data(data)
        else:
            # update with new data
            data.update(new_data)
            write_data(data)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)


def search_password():
    website = website_input.get()
    if len(website) == 0:
        messagebox.showinfo(title="Oops", message="Website field is empty.")
        return
    try:
        with open("data.json", mode="r") as file:
            data = json.load(file)

    except FileNotFoundError:
        messagebox.showinfo(title="Oops", message="You have not any saved passwords.")
    else:
        if website in data:
            email = data[website.lower()]["email"]
            password = data[website.lower()]["password"]
            messagebox.showinfo(
                title=website.title(), message=f"Email: {email}\nPassword: {password}"
            )
            website_input.delete(0, END)
        else:
            messagebox.showinfo(
                title="Error", message=f"No details for {website} exits."
            )


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
logo = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo)

canvas.grid(column=1, row=0)

website_label = Label(text="website:")
website_label.grid(column=0, row=1)

email_or_username_label = Label(text="Email/Username:")
email_or_username_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

website_input = Entry(width=21)
website_input.focus()
website_input.grid(
    column=1,
    row=1,
)

email_or_username_input = Entry(width=35)
email_or_username_input.insert(0, "manoj@gmail.com")
email_or_username_input.grid(column=1, row=2, columnspan=2)

password_input = Entry(width=21)
password_input.grid(column=1, row=3)

search_password_btn = Button(text="Search", command=search_password)
search_password_btn.grid(column=2, row=1)

generate_password_btn = Button(text="Generate Password", command=generate_password)
generate_password_btn.grid(column=2, row=3)

add_btn = Button(text="Add", width=36, command=save_password)
add_btn.grid(column=1, row=4, columnspan=2)

window.mainloop()
