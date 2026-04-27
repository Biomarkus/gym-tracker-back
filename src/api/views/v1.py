from flask import Blueprint
from flask_restful import Api

from src.api.resources.categories_api import CategoriesApi
from src.api.resources.exercises_api import ExercisesApi
from src.api.resources.exercises_api_multiple import ExercisesApiMultiple
from src.api.resources.session_exercises_api import SessionExercisesApi
from src.api.resources.session_exercises_by_id_api import SessionExercisesByIdApi
from src.api.resources.session_filter_api import SessionFilterApi
from src.api.resources.sessions_api import SessionsApi

api_v1_bp = Blueprint('api_v1', __name__, url_prefix='/api/v1')
api_v1 = Api(api_v1_bp)

api_v1.add_resource(SessionsApi, '/sessions') #POST
api_v1.add_resource(SessionFilterApi, '/session/filter') #POST
api_v1.add_resource(SessionExercisesApi, '/session-exercise')
api_v1.add_resource(SessionExercisesByIdApi, '/session/<int:session_id>/exercises')
api_v1.add_resource(CategoriesApi, '/categories') #GET POST
api_v1.add_resource(ExercisesApi, '/exercises') #GET POST
api_v1.add_resource(ExercisesApiMultiple, '/exercises/all') #POST
