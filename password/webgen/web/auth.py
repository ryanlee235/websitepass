from flask import Blueprint

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    pass

@auth.route('/newuser')
def create_user():
    pass
