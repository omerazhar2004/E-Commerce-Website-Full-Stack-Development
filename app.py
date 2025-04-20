from website import makeWebsite
app = makeWebsite()

if __name__ == '__main__':
    app.run(debug=True)
# from flask import Flask, render_template, request
# from flask_wtf import FlaskForm
# from wtforms import StringField, SubmitField
# from wtforms.validators import DataRequired, Length
# from flask_bootstrap import Bootstrap
# from flask_sqlalchemy import SQLAlchemy
# from models import Technology, cartItems

# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'top secret!'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.sqlite3'
# bootstrap = Bootstrap(app)
# db = SQLAlchemy(app)

# class Technology(db.Model):
#     _tablename_ = 'technologies'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column('name', db.String())
#     price = db.Column('price', db.Float())
#     description = db.Column('description', db.String())
#     img_loc = db.Column('img_loc', db.String())
#     carts = db.relationship('cartItems', backref=db.backref('technology', lazy=True))   #relationship between Technology and cartItems

# class cartItems(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     quantity = db.Column(db.Integer, nullable = False)

#     product_link = db.Column(db.Integer, db.ForeignKey('technology.id'), nullable=False)




# class OpinionForm(FlaskForm):
#     opinion = StringField('Quantity: ',validators = [DataRequired(),Length(min=0,max=100)])
#     submit = SubmitField('Submit')  

# @app.route('/')
# def galleryPage():
#     techs = Technology.query.all()
#     return render_template('index.html',technologies = techs)



# @app.route('/tech/<int:techId>', methods=['GET','POST'])

# def singleProductPage(techId):
#     form = OpinionForm()
#     tech = Technology.query.get(techId)
#     # if form.is_submitted():
#     #     data = form.opinion.data
#     #     return render_template('SingleTechOpinion.html', technology = tech,opinion = data)
#     # else:
#     return render_template('SingleTech.html', technology = tech, form = form)

# if __name__ == '__main__':
#     app.run(debug=True)
