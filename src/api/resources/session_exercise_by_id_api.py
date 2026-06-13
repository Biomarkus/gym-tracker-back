from http import HTTPStatus

from flask import abort
from flask_restful import Resource

from src.exceptions.session_exercise_exception import SessionExerciseNotFound
from src.repository import session_exercise as session_exercise_repository


class SessionExerciseByIdApi(Resource):
    def delete(self, session_exercise_id: int) -> dict:
        try:
            if not session_exercise_repository.get_session_exercises_by_filters({'id': session_exercise_id}).scalar():
                raise SessionExerciseNotFound(details=f"Session exercise with id: {session_exercise_id} not found.")
            session_exercise_repository.delete_session_exercises(session_exercise_id)

            return {'message': f'Session exercise with id: {session_exercise_id} deleted successfully.'}
        except SessionExerciseNotFound as exc:
            abort(HTTPStatus.NOT_FOUND, description=str(exc.details))