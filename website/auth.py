from flask import Blueprint
from flask import Flask, render_template, request, flash, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from .models import user
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_required, login_remembered, logout_user, current_user

from .models import Technology

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password') 

        user_check = user.query.filter_by(email = email).first()
        if user_check:
            if check_password_hash(user_check.password, password):
                flash('You logged in successfully!', category='success')
                login_user(user_check, remember=True)
                return redirect(url_for('nav.homePage')) 
            else:
                flash('password is not correct.', category='error')
        else:
            flash('Invalid email.', category='error')              
    return render_template('login.html', c_user = current_user)

@auth.route('/logout')
@login_required

def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['GET', 'POST'])
def signUp():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('fName')
        lastName = request.form.get('lName')
        password = request.form.get('password')  
        passwordConfirm = request.form.get('password2')  
        user_valid = user.query.filter_by(email = email).first()
        if user_valid:
            flash('email has already been registered', category='error')
        elif len(email) < 3:
            flash('invalid email entered. Enter again.', category='error')
        elif len(password) < 6:
            flash('Password is too short.', category='error')
        elif password != passwordConfirm:
            flash('Passwords donot match!', category='error')
        else:
            reg_user = user(email = email, fName = firstName, password = generate_password_hash(password, method='pbkdf2:sha256'))
            db.session.add(reg_user)
            db.session.commit()
            # login_user(user_valid, remember=True)
            flash('Account created successfully!', category='success') 
            return redirect(url_for('nav.homePage'))   
    return render_template('sign-up.html', c_user = current_user)


@auth.route('/adminItems', methods=['GET', 'POST'])
@login_required
def add_items():
    if request.method == 'POST':
        name = request.form.get('name')
        price = request.form.get('price') 
        description = request.form.get('description') 
        img_loc = request.form.get('img_loc') 
        item_check = Technology.query.filter_by(name = name).first()
        if current_user.id == 1:
            if item_check:
                flash('Item already exists in database!', category='error') 
            else:
                try:
                    reg_item = Technology(name = name, price = price, description = description, img_loc = f'/static/{img_loc}')
                    db.session.add(reg_item)
                    db.session.commit()
                    flash('Item added successfully for users to browse through.', category='success') 
                    return redirect('/adminItems')
                except Exception as e:
                    print("item could not be added to the main database.", e)
                    flash('item not added to the main database, kindly enter valid item informtation.', category='error')
        else:
            flash('Only an admin can add items to the main database.', category='error')               
    return render_template('adminItems.html', c_user = current_user)
