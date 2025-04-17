from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'top secret!'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.sqlite3'
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)

# app = Flask(__name__)
# app.config['SECRET_KEY'] = "top secret password don't tell anyone this"

# technologies = [
#     { "name": "Stick Cooking Pan", "Price": "28 £", "description": "Effortlessly cook and clean with our premium non-stick pan. Even heat distribution for perfect meals every time.", "img_loc": "/static/Stick cooking pan.jpeg"},
#     { "name": "Ski Jacket", "Price": "40 £", "description": "Stay warm and dry with our high-performance ski jacket. Advanced insulation and breathable waterproof design for ultimate comfort.", "img_loc": "/static/Ski Jacket.jpeg"},
#     { "name": "Mountain Bike", "Price": "699.99 £", "description": "Explore rugged terrains with our durable mountain bike. Lightweight frame, responsive suspension, and precision gearing for total control.", "img_loc": "/static/Mountain Bike.jpeg" },
# ]
class Technology(db.Model):
    _tablename_ = 'technologies'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column('name', db.String())
    price = db.Column('price', db.String())
    description = db.Column('description', db.String())
    img_loc = db.Column('img_loc', db.String())
class OpinionForm(FlaskForm):
    opinion = StringField('Your Opinion: ',validators = [DataRequired(),Length(min=0,max=100)])
    submit = SubmitField('Submit')
# @app.route('/')
# def index():
#     techs = technologies.query.all()
#     return render_template('index.html', technologies = techs)    

@app.route('/')
def galleryPage():
    techs = Technology.query.all()
    return render_template('index.html',technologies = techs)



@app.route('/tech/<int:techId>', methods=['GET','POST'])
# def singleProductPage(techId):
#     return render_template('SingleTech.html', technology = technologies[techId])
def singleProductPage(techId):
    form = OpinionForm()
    techs = Technology.query.all()
    if form.is_submitted():
        data = form.opinion.data
        return render_template('SingleTechOpinion.html', technology = techs,opinion = data)
    else:
        return render_template('SingleTech.html', technology = techs, form = form)

if __name__ == '__main__':
    app.run(debug=True)
