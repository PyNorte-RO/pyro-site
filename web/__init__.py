from flask import Flask

from .controllers import api


def create_app(debug=False):
    app = Flask(__name__)
    app.debug = debug
    app.register_blueprint(api)
    return app
