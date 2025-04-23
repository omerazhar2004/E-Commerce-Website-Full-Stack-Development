from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from . import db
from sqlalchemy.sql import func

class user(db.Model, UserMixin):
     id = db.Column(db.Integer, primary_key=True)
     email = db.Column(db.String(150), unique=True)
     password = db.Column(db.String(150))
     fName = db.Column(db.String(150))

     user_cart = db.relationship('cartItems', backref=db.backref('user', lazy=True))   #relationship between user and their respective cartItems
    

class Technology(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    price = db.Column(db.Float())
    description = db.Column(db.String(300))
    img_loc = db.Column(db.String(150))

    carts = db.relationship('cartItems', backref=db.backref('technology', lazy=True))   #relationship between Technology and cartItems

class cartItems(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer, nullable = False)

    product_link = db.Column(db.Integer, db.ForeignKey('technology.id'), nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

