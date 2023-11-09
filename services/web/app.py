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
    db.session.commit()



if __name__ == "__main__":
    cli()
