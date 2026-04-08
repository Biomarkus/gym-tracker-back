from flask import Flask
from flask_restful import Api
from src.api.views.v1 import register_routes


def create_app() -> Flask:
    app: Flask = Flask(__name__)
    api: Api = Api(app)

    register_routes(app=api)
    return app