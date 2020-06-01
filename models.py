import os
from sqlalchemy import Column, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy
import json

database_path = os.environ.get('DATABASE_URL')
if not database_path:
    database_name = "capstone"
    database_path = "postgres://yrpcnaiekvajor:43479be064d4b98b94f1b3ec45c2a7421f37929fd6865f3b181711df7b876c96@ec2-54-86-170-8.compute-1.amazonaws.com:5432/d2rj2k4mvc0n78"
# database_path = "postgres://{}/{}".format('localhost:5432', database_name)
db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''


def drop_create_all():
    db.drop_all()
    db.create_all()


def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()


class Ingredient(db.Model):
    __tablename__ = "ingredients"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    image_link = Column(String)
    color = Column(String)

    def __init__(self, name, image_link, color):
        self.name = name
        self.image_link = image_link
        self.color = color

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            "id": self.id,
            "name": self.name,
            "image_link": self.image_link,
            "color": self.color
        }


class Dish(db.Model):
    __tablename__ = "dishes"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=True)
    image_link = Column(String)
    # ingredients = db.relationship('Ingredients', backref='dishes', lazy='dynamic')
    ingredients = Column(String, nullable=False)

    def __init__(self, name, image_link, ingredients):
        self.name = name
        self.image_link = image_link
        self.ingredients = ingredients

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            "id": self.id,
            "name": self.name,
            "image_link": self.image_link,
            "ingredients": json.loads(self.ingredients)
        }
