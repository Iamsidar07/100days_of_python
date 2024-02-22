import pandas as pd
from flask import Flask, redirect, render_template, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField, TimeField, URLField
from wtforms.validators import URL, DataRequired

from cafe import Cafe

app = Flask(__name__)
app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe_name = StringField("Cafe name", validators=[DataRequired()])
    location_url = URLField(label="Location", validators=[DataRequired(), URL()])
    open_time = TimeField(label="Open time", validators=[DataRequired()])
    closing_time = TimeField(label="Closing time", validators=[DataRequired()])
    wifi_rating = SelectField(
        label="Wifi rating",
        choices=["✘", "💪", "💪💪", "💪💪💪", "💪💪💪💪", "💪💪💪💪💪"],
        validators=[DataRequired()],
    )
    coffee_rating = SelectField(
        label="Coffee rating",
        choices=["☕️", "☕☕", "☕☕☕", "☕☕☕☕", "☕☕☕☕☕"],
        validators=[DataRequired()],
    )
    power_outlet_rating = SelectField(
        label="Power rating",
        choices=["✘", "🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"],
        validators=[DataRequired()],
    )
    submit = SubmitField("Submit")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/add", methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open("cafe-data.csv", mode="a", encoding="utf-8") as file:
            file.write(
                f"\n{form.cafe_name.data},"
                f"{form.location_url.data},"
                f"{form.open_time.data},"
                f"{form.closing_time.data},"
                f"{form.coffee_rating.data},"
                f"{form.wifi_rating.data},"
                f"{form.power_outlet_rating.data}"
            )
        return redirect(url_for("cafes"))
    return render_template("add.html", form=form)


@app.route("/cafes")
def cafes():
    data = pd.read_csv("cafe-data.csv")
    list_of_rows = [value for (key, value) in data.iterrows()]
    list_of_cafes = []
    for row in list_of_rows:
        new_cafe = Cafe(
            cafe_name=row["Cafe Name"],
            location_url=row["Location"],
            open_time=row["Open"],
            closing_time=row["Close"],
            wifi_rating=row["Wifi"],
            coffee_rating=row["Coffee"],
            power_outlet_rating=row["Power"],
        )
        list_of_cafes.append(new_cafe)

    return render_template("cafes.html", cafes=list_of_cafes)


if __name__ == "__main__":
    app.run(debug=True)
