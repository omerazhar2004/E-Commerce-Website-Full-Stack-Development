from flask import Blueprint
from flask import Flask, render_template, request
from .models import Technology

nav = Blueprint('nav', __name__)

@nav.route('/')
def homePage():
    return render_template('home.html')
@nav.route('/gallery-page')
def galleryPage():
    techs = Technology.query.all()
    return render_template('index.html', technologies=techs)