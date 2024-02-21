from flask import Flask, render_template
import requests
from post import Post

app = Flask(__name__)
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


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/post/<int:post_id>")
def show_post(post_id):
    requested_post = None
    for post in all_posts:
        if post.id == post_id:
            requested_post = post

    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
