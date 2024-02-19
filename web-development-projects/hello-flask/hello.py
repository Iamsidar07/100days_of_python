from flask import Flask

app = Flask(__name__)

def make_bold(func):
    def wrapper_func():
        result = func()
        return f"<b>{result}</b>"
    return wrapper_func

def make_emphasis(func):
    def wrapper_func():
        result = func()
        return f"<em>{result}</em>"
    return wrapper_func

def make_underlined(func):
    def wrapper_func():
        result = func()
        return f"<u>{result}</u>"
    return wrapper_func

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def bye():
    return "Bye Home!!!"

@app.route("/username/<string:name>")
def username(name):
    return f"Hello, {name}"

if __name__ == "__main__":
    app.run(debug=True)
