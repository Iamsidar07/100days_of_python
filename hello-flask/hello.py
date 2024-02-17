from flask import Flask

app = Flask(__name__)

print("__name__", __name__)


@app.route("/")
def hello_word():
    return 'hello world'


if __name__ == "__main__":
    app.run()
