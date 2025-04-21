from flask import Blueprint
from flask import Flask, render_template, request
from .models import Technology
from flask_login import login_required, current_user

nav = Blueprint('nav', __name__)

@nav.route('/')
@login_required
def homePage():
    return render_template('home.html', c_user = current_user)
@nav.route('/gallery-page')
@login_required
def galleryPage():
    techs = Technology.query.all()
    return render_template('index.html', technologies=techs, c_user = current_user)