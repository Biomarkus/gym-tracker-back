from flask_restful import Api

from src.api.resources.categories_api import CategoriesApi
from src.api.resources.exercises_api import ExercisesApi
from src.api.resources.exercises_api_multiple import ExercisesApiMultiple
from src.api.resources.session_exercises_api import SessionExercisesApi
from src.api.resources.session_exercises_by_id_api import SessionExercisesByIdApi
from src.api.resources.session_filter_api import SessionFilterApi
from src.api.resources.sessions_api import SessionsApi


def register_routes(app: Api):
    app.add_resource(SessionsApi, '/sessions') #POST
    app.add_resource(SessionFilterApi, '/session/filter') #POST
    app.add_resource(SessionExercisesApi, '/session-exercise')
    app.add_resource(SessionExercisesByIdApi, '/session/<int:session_id>/exercises')
    app.add_resource(CategoriesApi, '/categories') #GET POST
    app.add_resource(ExercisesApi, '/exercises') #GET POST
    app.add_resource(ExercisesApiMultiple, '/exercises/all') #POST
