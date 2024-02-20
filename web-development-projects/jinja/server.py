from flask import Flask, render_template
import random
import requests

AGIFY_ENDPOINT = "https://api.agify.io"
GENDERIZE_ENDPOINT = "https://api.genderize.io"
BLOG_ENDPOINT = "https://api.npoint.io/c790b4d5cab58020d391"


app = Flask(__name__)


def get_gender(name):
    params = {"name": name}
    response = requests.get(GENDERIZE_ENDPOINT, params=params)
    response.raise_for_status()
    data = response.json()
    return data["gender"]


def get_age(name):
    params = {"name": name}
    response = requests.get(AGIFY_ENDPOINT, params=params)
    response.raise_for_status()
    data = response.json()
    return data["age"]


@app.route("/")
def home():
    random_number = random.randint(1, 10)
    print(random_number)
    return render_template("index.html", num=random_number)


@app.route("/guess/<string:name>")
def guess(name):
    age = get_age(name)
    gender = get_gender(name)
    return render_template("guess.html", name=name.title(), gender=gender, age=age)


@app.route("/blog")
def get_blog():
    response = requests.get(BLOG_ENDPOINT)
    response.raise_for_status()
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
