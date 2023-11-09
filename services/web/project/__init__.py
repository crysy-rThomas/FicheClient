from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object("project.config.Config")
db = SQLAlchemy(app)



class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=False, nullable=False)
    phone = db.Column(db.Integer, unique=True, nullable=False)
    adress = db.Column(db.String(128), unique=False, nullable=False)
    city = db.Column(db.String(128), unique=False, nullable=False)
    zipCode = db.Column(db.String(128), unique=False, nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
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
