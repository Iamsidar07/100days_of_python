from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
import os

OMDB_API_KEY = os.environ["OMDB_API_KEY"]
OMDB_ENDPOINT = "http://www.omdbapi.com/"


class Base(DeclarativeBase):
    pass


class RateMovieForm(FlaskForm):
    rating = StringField(label="Your rating out of 10 eg. 7.5", validators=[DataRequired()])
    review = StringField(label="Your review", validators=[DataRequired()])
    submit = SubmitField(label="Done")


class AddMovieForm(FlaskForm):
    title = StringField(label="Movie Title", validators=[DataRequired()])
    submit = SubmitField(label="Add Movie")


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///top-movies.db"
Bootstrap5(app)

# CREATE DB
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CREATE MODEL
class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(nullable=True)
    rating: Mapped[float] = mapped_column(Float, nullable=False)
    ranking: Mapped[int] = mapped_column(Integer, nullable=True)
    review: Mapped[str] = mapped_column(nullable=True)
    img_url: Mapped[str] = mapped_column(nullable=False)


# CREATE TABLE
with app.app_context():
    db.create_all()
    # ADD RECORD
    # new_movie = Movie(
    #     title="Phone Booth",
    #     year=2002,
    #     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an "
    #                 "extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with "
    #                 "the caller leads to a jaw-dropping climax.",
    #     rating=7.3,
    #     ranking=10,
    #     review="My favourite character was the caller.",
    #     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
    # )
    # db.session.add(new_movie)
    # db.session.commit()


@app.route("/")
def home():
    all_movies = db.session.execute(db.select(Movie).order_by(Movie.rating)).scalars().all()
    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()
    return render_template("index.html", movies=all_movies)


@app.route("/edit", methods=["GET", "POST"])
def edit():
    form = RateMovieForm()
    movie_id = request.args.get("id")
    movie = db.get_or_404(Movie, movie_id)
    if form.validate_on_submit():
        movie.rating = float(form.rating.data)
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for("home"))

    return render_template("edit.html", movie=movie, form=form)


@app.route("/delete")
def delete_movie():
    movie_id = request.args.get("id")
    movie_to_delete = db.get_or_404(Movie, movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/add", methods=["GET", "POST"])
def add_movie():
    form = AddMovieForm()
    if form.validate_on_submit():
        movie_title = form.title.data
        params = {
            "apikey": OMDB_API_KEY,
            "s": movie_title,
            "r": "json"
        }
        response = requests.get(url=OMDB_ENDPOINT, params=params)
        response.raise_for_status()
        search_results = response.json()["Search"]
        return render_template("select.html", results=search_results)
    return render_template("add.html", form=form)


@app.route("/get-movie-detail")
def get_movie_detail():
    imdb_id = request.args.get("id")
    params = {
        "apikey": OMDB_API_KEY,
        "i": imdb_id,
        "r": "json"
    }
    response = requests.get(url=OMDB_ENDPOINT, params=params)
    movie = response.json()
    new_movie = Movie(
        title=movie["Title"],
        year=int(movie["Year"]),
        description=movie["Plot"],
        rating=float(movie["imdbRating"]),
        img_url=movie["Poster"],
        ranking=1,
        review="My favourite character was the caller.",
    )
    db.session.add(new_movie)
    db.session.commit()
    return redirect(url_for("edit", id=new_movie.id))


if __name__ == '__main__':
    app.run(debug=True)
