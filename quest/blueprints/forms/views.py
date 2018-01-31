from flask import Blueprint, render_template

forms = Blueprint('form', __name__, template_folder='templates')



@forms.route('/signup')
def signup():
    return render_template('forms/signup.html')


@forms.route('/login')
def login():
    return render_template('forms/login.html')
