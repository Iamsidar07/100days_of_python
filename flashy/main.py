from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
TIMER = 3000
try:
    data = pd.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("./data/french_words.csv")
finally:
    to_learn = data.to_dict(orient="records")
current_card = {}


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    french_word = current_card["French"]
    canvas.itemconfig(card_background, image=card_front_img)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=french_word, fill="black")
    flip_timer = window.after(TIMER, func=flip_card)


def flip_card():
    global current_card
    english_word = current_card["English"]
    canvas.itemconfig(card_background, image=card_back_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=english_word, fill="white")


def is_known():
    to_learn.remove(current_card)
    df = pd.DataFrame(to_learn)
    df.to_csv("./data/words_to_learn.csv", index=False)
    next_card()


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(TIMER, func=flip_card)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas.grid(column=0, row=0, columnspan=2)

card_back_img = PhotoImage(file="./images/card_back.png")
card_front_img = PhotoImage(file="./images/card_front.png")
card_background = canvas.create_image(400, 263, image=card_front_img)

card_title = canvas.create_text(400, 153, text="Text", font=("Monolisa", 30, "italic"))
card_word = canvas.create_text(400, 260, text="Word", font=("Monolisa", 34, "bold"))

wrong_img = PhotoImage(file="./images/wrong.png", )
unknown_btn = Button(image=wrong_img, highlightthickness=0, command=next_card)
unknown_btn.grid(row=1, column=0)

right_img = PhotoImage(file="./images/right.png")
known_btn = Button(image=right_img, highlightthickness=0, command=is_known)
known_btn.grid(row=1, column=1)

next_card()
window.mainloop()
