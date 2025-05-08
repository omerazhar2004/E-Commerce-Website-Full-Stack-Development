from flask import Blueprint
from flask import Flask, render_template, request, flash, url_for, redirect
from .models import Technology, cartItems, user
from flask_login import login_required, current_user
from . import db

nav = Blueprint('nav', __name__)

@nav.route('/', methods=['GET', 'POST'])
@login_required
def homePage(filter_by = None, filter_by_price = None, filter_by_env_impact = None):
    if request.method == 'POST':
        filter_by = request.form.get('filter_by') 
        filter_by_price = request.form.get('filter_by_price')
        filter_by_env_impact = request.form.get('filter_by_env_impact')
    if filter_by:
        techs = Technology.query.filter(Technology.name.ilike(f'{filter_by}%'))
    elif filter_by_price:
        techs = Technology.query.filter(Technology.price.ilike(f'{filter_by_price}%'))
    elif filter_by_env_impact:
          techs = Technology.query.filter(Technology.env_impact.ilike(f'{filter_by_env_impact}%'))
    else:       
        techs = Technology.query.all()
    return render_template('home.html', technologies=techs, c_user = current_user)

@nav.route('/references')
def refPage():
    return render_template('references.html', c_user = current_user)


@nav.route('/cartItems')
@login_required
def cart_page():
    c_items = cartItems.query.filter_by(user_id = current_user.id).all()
    total_price = 0
    overall_total_price = 0
    for item in c_items:
        total_price = item.technology.price * item.quantity
        overall_total_price += total_price    
    return render_template('cart.html', c_techs = c_items, c_user = current_user, total_price = total_price, overall_total_price = overall_total_price)

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

@nav.route('/checkout', methods=['GET', 'POST'])
def checkoutPage():
    cart_vars = cart_page()
    if request.method == 'POST':
        card_number = request.form.get('card-number')
        cv = request.form.get('cv')
        if len(card_number) < 16:
            flash('invalid card number.', category='error')
        elif len(cv) < 3:
            flash('Invalid CV number.', category='error')
        else:
            flash('You have checked out successfully!', category='success') 
            return redirect(url_for('nav.homePage'))   
    return render_template('checkout.html', c_user = current_user, cart_vars = cart_vars)

@nav.route('/individual-item/<int:techId>')
@login_required
def individual_item_page(techId):
    item_detail = Technology.query.filter_by(id=techId).first() 
    return render_template('individual_item.html', c_user = current_user, item_detail = item_detail)

        

