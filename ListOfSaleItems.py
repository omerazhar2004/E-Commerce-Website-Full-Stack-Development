from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
from flask_bootstrap import Bootstrap
from flask import Flask, render_template, request
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'top secret!'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
# Base = declarative_base()

# Base = declarative_base
class Technology(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column('name', db.String())
    price = db.Column('price', db.String())
    description = db.Column('description', db.String())
    img_loc = db.Column('img_loc', db.String())
    
    def __init__(self, name, price, description, img_loc):
        self.name = name
        self.price = price
        self.description = description
        self.img_loc = img_loc
        # return f"{self.name} / {self.price} / {self.description} / {self.img_loc}" 
with app.app_context():
    db.create_all()
# technologies = [
#             { "name": "Stick Cooking Pan", "price": "28 £", "description": "Effortlessly cook and clean with our premium non-stick pan. Even heat distribution for perfect meals every time.", "img_loc": "/static/Stick cooking pan.jpeg"},
#             { "name": "Ski Jacket", "price": "40 £", "description": "Stay warm and dry with our high-performance ski jacket. Advanced insulation and breathable waterproof design for ultimate comfort.", "img_loc": "/static/Ski Jacket.jpeg"},
#             { "name": "Mountain Bike", "price": "699.99 £", "description": "Explore rugged terrains with our durable mountain bike. Lightweight frame, responsive suspension, and precision gearing for total control.", "img_loc": "/static/Mountain Bike.jpeg" },
#         ]        

# with app.app_context():
#     db.create_all()
#     for tech in technologies:
#             new_tech = Technology(name=tech["name"], price=tech["price"], description=tech["description"], img_loc=tech["img_loc"])
#             db.session.add(new_tech)
#             db.session.commit()
        # engine = create_engine('sqlite:///technologies.db')
        # Base.metadata.create_all(engine)

        # Session = sessionmaker(bind = engine)
        # session = Session()
        # technologies = [
        #     { "name": "Stick Cooking Pan", "Price": "28 £", "description": "Effortlessly cook and clean with our premium non-stick pan. Even heat distribution for perfect meals every time.", "img_loc": "/static/Stick cooking pan.jpeg"},
        #     { "name": "Ski Jacket", "Price": "40 £", "description": "Stay warm and dry with our high-performance ski jacket. Advanced insulation and breathable waterproof design for ultimate comfort.", "img_loc": "/static/Ski Jacket.jpeg"},
        #     { "name": "Mountain Bike", "Price": "699.99 £", "description": "Explore rugged terrains with our durable mountain bike. Lightweight frame, responsive suspension, and precision gearing for total control.", "img_loc": "/static/Mountain Bike.jpeg" },
        # ]
        # with app.app_context():
        #     for tech in technologies:
        #         new_tech = technologies(name = tech["name"], price = tech["Price"], description = tech["description"], img_loc = tech["img_loc"])
        #         db.session.add(new_tech)
        #         db.session.add(new_tech)
        #         db.session.commit()
        #     print("Technologies have been added to the database.")
@app.route('/')
def index():
    techs = Technology.query.all()
    return render_template('index.html', technologies = techs)

if __name__ == '__main__':
    app.run(debug=True,port=5050)


























































































































        