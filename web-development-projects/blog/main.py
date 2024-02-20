from flask import Flask, render_template
import requests
from post import Post


blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
app = Flask(__name__)

response = requests.get(blog_url)
response.raise_for_status()
posts = response.json()

post_objects = []
for post in posts:
    new_post = Post(
        id=post["id"], title=post["title"], subtitle=post["subtitle"], body=post["body"]
    )
    post_objects.append(new_post)


@app.route("/")
def get_all_posts():
    return render_template("index.html", posts=post_objects)


@app.route("/post/<int:post_id>")
def show_post(post_id):
    requested_post = None
    for post in post_objects:
        if post.id == post_id:
            requested_post = post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
