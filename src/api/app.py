from flask import Flask

from src.api.views.v1 import api_v1_bp


def create_app() -> Flask:
    app: Flask = Flask(__name__)
    app.register_blueprint(api_v1_bp)
    return app