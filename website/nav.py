from flask import Blueprint
from flask import Flask, render_template, request, flash, url_for, redirect
from .models import Technology, cartItems, user
from flask_login import login_required, current_user
from . import db

nav = Blueprint('nav', __name__)

@nav.route('/', methods=['GET', 'POST'])
@login_required
def homePage(filter_by = None):
    if request.method == 'POST':
        filter_by = request.form.get('filter_by') 
    if filter_by:
        techs = Technology.query.filter(Technology.name.ilike(f'{filter_by}%'))
    else:       
        techs = Technology.query.all()
    return render_template('home.html', technologies=techs, c_user = current_user)

@nav.route('/cartItems')
@login_required
def cart_page():
    c_items = cartItems.query.filter_by(user_id = current_user.id).all()
    total_price = 0
    for item in c_items:
        total_price = item.technology.price * item.quantity
    return render_template('cart.html', c_techs = c_items, c_user = current_user, total_price = total_price)

@nav.route('/append-to-cart/<int:item_id>')
@login_required
def add_to_cart(item_id):
    item_add = Technology.query.get(item_id)
    cart_item_check = cartItems.query.filter_by(product_link = item_id, user_id=current_user.id).first()
    if cart_item_check:
        cart_item_check.quantity += 1
        db.session.commit()
        flash(f'quantity of {cart_item_check.technology.name} has been increased in your cart.', category='success')
        return redirect(url_for('nav.homePage'))
    reg_cart_item = cartItems(quantity = 1, product_link = item_add.id, user_id = current_user.id)   
    db.session.add(reg_cart_item)
    db.session.commit()
    flash(f'{reg_cart_item.technology.name} has been added to the cart', category='success')
    return redirect(url_for('nav.homePage'))
    return render_template('home.html', c_user = current_user)

@nav.route('/delete-from-cart/<int:item_id>')
@login_required
def delete_from_cart(item_id):
    try:
        item_delete = cartItems.query.get(item_id)
        db.session.delete(item_delete)
        db.session.commit()
        flash('item removed from cart successfully.', category='success')
        return redirect(url_for('nav.cart_page'))
    except Exception as e:
        flash('item could not be removed from the cart.', category='error') 
        return redirect(url_for('nav.cart_page'))
    return render_template('cart.html', c_user = current_user)
        

