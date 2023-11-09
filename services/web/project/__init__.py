from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object("project.config.Config")
db = SQLAlchemy(app)



class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=False, nullable=False)
    phone = db.Column(db.Integer, unique=True, nullable=True)
    adress = db.Column(db.String(128), unique=False, nullable=True)
    city = db.Column(db.String(128), unique=False, nullable=True)
    zipCode = db.Column(db.String(128), unique=False, nullable=True)
    email = db.Column(db.String(128), unique=True, nullable=True)
    active = db.Column(db.Boolean(), default=True, nullable=False)

    def __init__(self, name, phone, adress, city, zipCode,email, active=True):
        self.name = name
        self.phone = phone
        self.adress = adress
        self.city = city
        self.zipCode = zipCode
        self.email = email


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        #find user by name
        user = User.query.filter_by(name=request.form['name']).all()
        return render_template("index.html", contats=user)
    else:
        users = User.query.all()
        return render_template("index.html", contats=users)

@app.route("/voir/<int:id>", methods=["GET"])
def voir():
    user = User.query.filter_by(id=id).first()
    return render_template("voir.html", user=user)

@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit():


    if request.method == 'POST':
        #find user by id and update data
        return "WIP"
    else:
        user = User.query.filter_by(id=id).first()
        return render_template("edit.html", user=user)
