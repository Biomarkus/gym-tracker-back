from flask import Blueprint
from flask_restful import Api

from src.api.resources.categories_api import CategoriesApi
from src.api.resources.exercises_api import ExercisesApi
from src.api.resources.exercises_api_multiple import ExercisesApiMultiple
from src.api.resources.session_by_id_api import SessionByIdApi
from src.api.resources.session_exercises_by_id_api import SessionExercisesByIdApi
from src.api.resources.session_filter_api import SessionFilterApi
from src.api.resources.session_tags_api import SessionTagsApi
from src.api.resources.sessions_api import SessionsApi
from src.api.resources.session_exercise_by_id_api import SessionExerciseByIdApi

api_v1_bp = Blueprint('api_v1', __name__, url_prefix='/api/v1')
api_v1 = Api(api_v1_bp)

api_v1.add_resource(SessionsApi, '/sessions') #POST
api_v1.add_resource(SessionFilterApi, '/session/filter') #POST
api_v1.add_resource(SessionExercisesByIdApi, '/session/<int:session_id>/exercises') #GET #POST
api_v1.add_resource(SessionExerciseByIdApi, '/session-exercise/<int:session_exercise_id>') #DELETE
api_v1.add_resource(CategoriesApi, '/categories') #GET POST
api_v1.add_resource(ExercisesApi, '/exercises') #GET POST
api_v1.add_resource(ExercisesApiMultiple, '/exercises/all') #POST
api_v1.add_resource(SessionTagsApi, '/session-tags') #POST
api_v1.add_resource(SessionByIdApi, '/session/<int:session_id>') #GET PUT
