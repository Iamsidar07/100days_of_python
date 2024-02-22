from flask import Flask, render_template, request
import requests
from post import Post
from smtplib import SMTP
import os

app = Flask(__name__)
MY_EMAIL = os.environ.get("MY_EMAIL")
PASSWORD = os.environ.get("PASSWORD")
blog_url = "https://api.npoint.io/201b9c3699098dd901a2"
data = requests.get(blog_url).json()
all_posts = []
for item in data:
    new_post = Post(
        post_id=item["id"],
        post_title=item["title"],
        post_subtitle=item["subtitle"],
        author=item["author"],
        published_date=item["date"],
        body=item["body"],
        img_url=item["image_url"],
    )
    all_posts.append(new_post)


@app.route("/")
def get_all_posts():
    return render_template("index.html", posts=all_posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "GET":
        return render_template("contact.html")
    else:
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']
        msg = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}".encode("utf-8")
        # sent email
        with SMTP('smtp.gmail.com', port=587) as connection:
            connection.starttls()
            connection.login(
                user=MY_EMAIL,
                password=PASSWORD,
            )
            connection.sendmail(
                from_addr=email,
                to_addrs=MY_EMAIL,
                msg=msg
            )
        return render_template("contact.html", success_msg="Successfully sent message")


@app.route("/post/<int:post_id>")
def show_post(post_id):
    requested_post = None
    for post in all_posts:
        if post.id == post_id:
            requested_post = post

    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
