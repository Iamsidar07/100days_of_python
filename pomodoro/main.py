# POMODORO Technique
# 25 min -> work
# 5 min -> break
# After 4 repetation
# 25 min -> break

from tkinter import *
import math


# CONSTANTS
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 25

timer = None
reps = 0

# Timer Reset


def reset_timer():
    global timer
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    checkmark_label.config(text="")
    global reps
    reps = 0


# Countdown Mechanism


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_session = math.floor(reps / 2)
        for _ in range(0, work_session):
            mark += "✔"

        checkmark_label.config(text=mark)


# UI Setup

window = Tk()
window.title("Pomodoro🍅")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomoto_img = PhotoImage(file="tomato.png")

canvas.create_image(100, 112, image=tomoto_img)
timer_text = canvas.create_text(
    103, 131, text="00:00", fill="white", font=(FONT_NAME, 36, "bold")
)
canvas.grid(column=1, row=1)


# Heading label
title_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, "normal"))
title_label.grid(column=1, row=0)


def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        title_label.config(text="Break", fg=PINK)
    else:
        count_down(WORK_MIN * 60)
        title_label.config(text="Work")


# Start button
# highlight thickness -> outline
start_btn = Button(text="Start", highlightthickness=0, command=start_timer)
start_btn.grid(column=0, row=2)


# Start button
reset_btn = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_btn.grid(column=2, row=2)

checkmark_label = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 14, "normal"))
checkmark_label.grid(column=1, row=3)

# At the end of program
window.mainloop()
