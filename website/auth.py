from flask import Blueprint
from flask import Flask, render_template, request, flash
from flask_login import login_user, login_required, logout_user, current_user
from .models import user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
# @auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/logout')
def logout():
    return render_template('logout.html')

@auth.route('/sign-up', methods=['GET', 'POST'])
def signUp():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('fName')
        lastName = request.form.get('lName')
        password = request.form.get('password')  
        passwordConfirm = request.form.get('password2')  

        if len(email) < 3:
            flash('invalid email entered. Enter again.', category='error')
        elif len(password) < 6:
            flash('Password is too short.', category='error')
        elif password != passwordConfirm:
            flash('Passwords donot match!', category='error')
        else:
            reg_user = user(email = email, password = password, fName = firstName)
            flash('Account created successfully!', category='success')    
    return render_template('sign-up.html')
