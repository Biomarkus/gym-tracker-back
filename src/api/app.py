from flask import Flask
from flask_restful import Api


def create_app() -> Flask:
    app: Flask = Flask(__name__)
    api: Api = Api(app)

    return app