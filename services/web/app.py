from flask.cli import FlaskGroup

from project import app, db, User


cli = FlaskGroup(app)


@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

@cli.command("seed_db")
def seed_db():
    db.session.add(User(name="Ryan THOMAS", phone="0102030405", adress="1 rue LundiMatin", city="Montpellier", zipCode="34000",email="ryan@thomas.fr"))
    db.session.add(User(name="Bob John", phone="0203040501", adress="2 rue LundiMatin", city="Montpellier", zipCode="34000",email="bob@john.com"))
    db.session.add(User(name="Alain Martin", phone="0103040501", adress="2 rue LundiMatin", city="Montpellier", zipCode="34000",email="AlMartin@gmail.com"))
    db.session.commit()



if __name__ == "__main__":
    cli()
