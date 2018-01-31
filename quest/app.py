from flask import Flask

from quest.blueprints.page import page
from quest.blueprints.forms import forms


def create_app():
    """
    Create a Flask application using the app factory pattern.

    :return: Flask app
    """
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object('config.settings')
    app.config.from_pyfile('settings.py', silent=True)

    app.register_blueprint(page)
    app.register_blueprint(forms)

    return app
