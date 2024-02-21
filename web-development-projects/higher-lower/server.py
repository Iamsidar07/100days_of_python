from flask import Flask
import random

app = Flask(__name__)
random_num = random.randint(0, 9)
print(random_num)


@app.route("/")
def home():
    return (
        "<h1>Guess a number between 0 and 9</h1>"
        '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" width=240/>'
    )


@app.route("/<int:guessed_num>")
def guess_num(guessed_num):
    print(random_num)
    if guessed_num > random_num:
        return (
            '<h1 style="color:purple;">Too high, try again!</h1>'
            '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" width=240/>'
        )
    elif guessed_num < random_num:
        return (
            '<h1 style="color:red;">Too Low, try again!</h1>'
            '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" width=240/>'
        )
    else:
        return (
            '<h1 style="color:green;">You found me!</h1>'
            '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" width=240/>'
        )


if __name__ == "__main__":
    app.run()
