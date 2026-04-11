from flask_restful import Api

from src.api.resources.session_exercises_api import SessionExercisesApi
from src.api.resources.session_filter_api import SessionFilterApi
from src.api.resources.sessions_api import SessionsApi


def register_routes(app: Api):
    app.add_resource(SessionsApi, '/sessions') #POST
    app.add_resource(SessionFilterApi, '/session/filter') #POST
    app.add_resource(SessionExercisesApi, '/session-exercise')
