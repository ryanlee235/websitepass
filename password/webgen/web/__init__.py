from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
# naming a variable and created the sqlalchmey
db = SQLAlchemy()
# setting the name to the database
DB_NAME = 'database.db'

#this is our main function that makes the whole app run
def create_app():
    #creates the flask app
    app = Flask(__name__)
    #this configures a secret key to make our website more secure
    app.config['SECRET_KEY'] = 'battlefield2042'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    #initialzing the database 
    db.init_app(app)
    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    #importing the blueprints
    from .auth import auth 
    from .views import views

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
        
    #need to set up the blueprints so we can run these in the app
    app.register_blueprint(auth)
    app.register_blueprint(views)
    from .models import User, Passwords
    #calling the create_database function 
    create_database(app)

    return app


#creates the database
def create_database(app):
    #if there is not a file in the website file path named database.db
    if not path.exists("website/" + DB_NAME):
        #create the data base
        db.create_all(app=app)
        print('created database!')
