from flask import Flask, render_template, request ,redirect
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
       #redirect to home if name is empty
        if request.form['name'] == '':
            return redirect("/")
         #find user that contains the name
        user = User.query.filter(User.name.contains(request.form['name'])).all()
        return render_template("index.html", contacts=user)
    else:
        contacts = User.query.all()
        return render_template("index.html", contacts=contacts)

@app.route("/voir/<int:id>", methods=["GET"])
def voir(id):
    user = User.query.filter_by(id=id).first()
    userName = user.name.split(' ')
    return render_template("voir.html", user=user, userName=userName)

@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    user = User.query.filter_by(id=id).first()
    userName = user.name.split(' ')
    if request.method == 'POST':
        user.name = request.form['name']
        user.phone = request.form['phone']
        user.adress = request.form['adress']
        user.city = request.form['city']
        user.zipCode = request.form['zipCode']
        user.email = request.form['email']

        try:
            db.session.commit()
            return redirect("/")
        except:
            return "There was a problem updating data."
    else:
        return render_template("edit.html", user=user, userName=userName)
