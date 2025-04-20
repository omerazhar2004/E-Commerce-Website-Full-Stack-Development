from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
DB_NAME = "dataStore.db"


db = SQLAlchemy()

def makeWebsite():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'top secret!'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)
    # bootstrap = Bootstrap(app)
    # db = SQLAlchemy(app)
    from .nav import nav
    from .auth import auth


    app.register_blueprint(nav, url_prefix = '/')
    app.register_blueprint(auth, url_prefix = '/')

    from .models import user, Technology, cartItems
    makeDataBase(app)
    return app

def  makeDataBase(app):
    if not path.exists('website/' + DB_NAME):
        with app.app_context():
            db.create_all()
            print('database created successfully.')
