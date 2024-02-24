from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
import random

app = Flask(__name__)


# CREATE DB
class Base(DeclarativeBase):
    pass


# Connect to Database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cafes.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self):
        result_dict = {}
        for column in self.__table__.columns:
            result_dict[column.name] = getattr(self, column.name)
        return result_dict


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route("/random")
def get_random_cafe():
    all_cafes = db.session.execute(db.select(Cafe)).scalars().all()
    random_cafe = random.choice(all_cafes)

    return jsonify(cafe=random_cafe.to_dict()), 200


# get all cafes
@app.route("/all")
def get_all_cafes():
    all_cafes = db.session.execute(db.select(Cafe)).scalars().all()
    all_cafes_dict = [cafe.to_dict() for cafe in all_cafes]
    return jsonify(cafes=all_cafes_dict), 200


# find a cafe by location
@app.route("/search")
def get_cafe_by_query():
    location = request.args.get("loc").title().strip()
    cafes = (
        db.session.execute(db.select(Cafe).where(Cafe.location == location))
        .scalars()
        .all()
    )
    cafes_dict = [cafe.to_dict() for cafe in cafes]
    if len(cafes) == 0:
        return jsonify(
            error={"Not Found": "Sorry, we don't have a cafe at that location."}
        )
    return jsonify(cafe=cafes_dict), 200


# HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def add_new_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("location"),
        seats=request.form.get("seats"),
        has_toilet=bool(request.form.get("has_toilet")),
        has_wifi=bool(request.form.get("has_wifi")),
        has_sockets=bool(request.form.get("has_sockets")),
        can_take_calls=bool(request.form.get("can_take_calls")),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added new cafe."}), 201


# HTTP PUT/PATCH - Update Record
@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update_cafe(cafe_id):
    new_price = request.args.get("new_price")
    cafe = db.get_or_404(Cafe, cafe_id)
    if cafe:
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(response={"success": "Successfully updated the price."}), 200
    return jsonify(
        error={"Not Found": "Sorry a cafe with that id does not exits in database."}
    ), 404


# HTTP DELETE - Delete Record
@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    apikey = request.args.get("apikey")

    def is_valid_apikey(api_key):
        return api_key == "TopSecretKey"

    if not is_valid_apikey(apikey):
        return jsonify(
            {"error": "Sorry, that's not allowed. Make sure that you've right apikey."}
        ), 403
    cafe_to_delete = db.get_or_404(Cafe, cafe_id)
    if cafe_to_delete:
        db.session.delete(cafe_to_delete)
        db.session.commit()
        return jsonify(
            response={"success": "Successfully deleted the cafe from database."}
        ), 200
    else:
        return jsonify(
            error={"Not Found": "Sorry a cafe with that id was not found in database."}
        ), 404


if __name__ == "__main__":
    app.run(debug=True)
