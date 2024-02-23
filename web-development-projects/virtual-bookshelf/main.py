from flask import Flask, render_template, request, redirect, url_for

# import database
# import sqlite3
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float


class Base(DeclarativeBase):
    pass


app = Flask(__name__)
db = SQLAlchemy(model_class=Base)
# db = sqlite3.connect("new-books-collection.db")

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books-collection.db"
db.init_app(app)


class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, unique=True, primary_key=True)
    title: Mapped[str] = mapped_column(
        String(250),
        unique=True,
        nullable=False,
    )
    author: Mapped[str] = mapped_column(
        String(250),
        nullable=False,
    )
    rating: Mapped[float] = mapped_column(Float, nullable=False)

    def __repr__(self):
        return f"<Book {self.title}>"


with app.app_context():
    db.create_all()

with app.app_context():
    all_books = db.session.execute(db.select(Book).order_by(Book.title)).scalars().all()

# book_id = 1
# create record
# with app.app_context():
# delete table
# db.drop_all()
# create new record
# new_book = Book(id=1, title="Harry Potter", author="J. K. Rowling", rating=9.3)
# db.session.add(new_book)
# db.session.commit()
# read all records
# result = db.session.execute(db.select(Book).order_by(Book.title))
# print(result)
# all_books = result.scalars()
# print(all_books)
# read a particular record by query
# result = db.session.execute(db.select(Book).where(Book.title == "Harry Potter"))
# single_book = result.scalar()
# print(result, single_book)
# update a record
# book_to_update = db.session.execute(db.select(Book).where(Book.title == "Harry Potter")).scalar()
# book_to_update.title = "Harry Potter and Chamber of Secrets"
# db.session.commit()
# print(book_to_update)
# update a record by primary key
# book_to_update = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
# book_to_update = db.get_or_404(Book, book_id)
# book_to_update.title = "Harry Porter Yan"
# db.session.commit()
# delete a record by primary key
# book_to_delete = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
# book_to_delete = db.get_or_404(Book, book_id)
# db.session.delete(book_to_delete)
# db.session.commit()
# pass


# connect to database
# db.init_app(app)
# create cursor which will control db
# cursor = db.cursor()

# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) "
#                "NOT NULL, rating FLOAT NOT NULL)")
#
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()


@app.route("/")
def home():
    return render_template("index.html", books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        # new_book = BookItem(
        #     title=request.form.get("title"),
        #     author=request.form.get("author"),
        #     rating=request.form.get("rating"),
        # )
        # all_books.append(new_book)
        with app.app_context():
            new_book = Book(
                title=request.form.get("title"),
                author=request.form.get("author"),
                rating=request.form.get("ratingng"),
            )
            db.session.add(new_book)
            db.session.commit()
        return redirect(url_for("home"))
    else:
        return render_template("add.html")


@app.route("/edit", methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        book_id = request.form["id"]
        book_to_update = db.get_or_404(Book, book_id)
        book_to_update.rating = request.form["rating"]
        db.session.commit()
        return redirect(url_for("home"))
    book_id = request.args.get("id")
    print(book_id)
    book_selected = db.get_or_404(Book, book_id)
    return render_template("edit.html", book=book_selected)


@app.route("/delete")
def delete_book():
    book_id = request.args.get("id")
    book_to_delete = db.get_or_404(Book, book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
