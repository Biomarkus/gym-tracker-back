from flask_restful import Resource

from models.session_exercise import SessionExercise
from src.repository import session_exercise as session_exercise_repository
from src.schemas.session_exercises.session_ex_response import SessionExerciseResponseModel


class SessionExercisesByIdApi(Resource):
    def get(self, session_id: int) -> list[dict]:
        session_exercises: list[SessionExercise] = session_exercise_repository \
        .get_session_exercises_by_filters({'session_id': session_id}).all()

        return [SessionExerciseResponseModel.model_validate(session_exercise).model_dump()
                for session_exercise in session_exercises]