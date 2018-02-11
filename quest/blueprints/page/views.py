from flask import Blueprint, render_template

page = Blueprint('page', __name__, template_folder='templates')


@page.route('/')
def home():
    return render_template('page/home.html')

@page.route('/index1')
def index1():
    return render_template('page/index1.html')



@page.route('/terms')
def terms():
    return render_template('page/terms.html')


@page.route('/privacy')
def privacy():
    return render_template('page/privacy.html')
