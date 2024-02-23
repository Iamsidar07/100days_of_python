from flask import Flask, render_template, request, redirect, url_for
from book import BookItem
# import database
import sqlite3
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float


class Base(DeclarativeBase):
    pass


all_books = []

app = Flask(__name__)
db = SQLAlchemy(model_class=Base)
# db = sqlite3.connect("new-books-collection.db")

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///random-books-collection.db"
db.init_app(app)


class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False, )
    author: Mapped[str] = mapped_column(String(250), nullable=False, )
    rating: Mapped[float] = mapped_column(Float, nullable=False)

    def __repr__(self):
        return f'<Book {self.title}>'


with app.app_context():
    db.create_all()

# create record
with app.app_context():
    new_book = Book(id=1, title="Harry Potter", author="J. K. Rowling", rating=9.3)
    db.session.add(new_book)
    db.session.commit()

# connect to database
# db.init_app(app)
# create cursor which will control db
# cursor = db.cursor()

# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) "
#                "NOT NULL, rating FLOAT NOT NULL)")
#
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()


@app.route('/')
def home():
    return render_template("index.html", books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        new_book = BookItem(
            title=request.form.get("title"),
            author=request.form.get("author"),
            rating=request.form.get("rating")
        )
        all_books.append(new_book)
        return redirect(url_for('home'))
    else:
        return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)
