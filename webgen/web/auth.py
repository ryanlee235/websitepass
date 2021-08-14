from flask import Blueprint, request, session, url_for, flash
from flask.templating import render_template
from werkzeug.utils import redirect
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

auth = Blueprint('auth', __name__)

#defining the url for the page, and the methods
@auth.route('/login', methods=['POST', "GET"])
def login():
    #if there is data being sent from the website
    if request.method =="POST":
        #get the email
        email = request.form.get("email")
        #get the password
        password = request.form.get("password")




@auth.route('/sign-up')
def create_user():
    return render_template("newuser.html")

