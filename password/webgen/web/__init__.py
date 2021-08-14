from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from os import path
#creating the database
db = SQLAlchemy()
#giving the database a name
DB_NAME = 'database.db'
#creating the app
def create_app():
    #this creates a flask application
    app = Flask(__name__)
    #configures a secret key for security reasons
    app.config['SECRET_KEY'] ='jfadsl;ksdapoi'
    app.config['SQLALCHEMY_DATABASE_URL'] = f'sqlite://{DB_NAME}'
    db.init_app(app)
    #importing the blue prints from the view and auth files
    from .views import views 
    from .auth import auth
    #initializing the blueprints for both of the files
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app


def create_database(app):
    if not path.exists("website/" + DB_NAME):
        db.create_all(app=app)
        print("Created database!")
