#user related routes here
from mainapp.users.forms import Userform
from flask import Blueprint


users = Blueprint('users', __name__)


@users.route("/dashboard", methods=['GET', 'POST'])
def homepage():

    pass