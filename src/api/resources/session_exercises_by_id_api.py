from flask_restful import Resource
from src.db.models.session_exercise import SessionExercise
from src.exceptions.session_exceptions import SessionNotFound
from src.repository import session_exercise as session_exercise_repository
from src.schemas.session_exercises.session_ex_response import SessionExerciseResponseModel
from http import HTTPStatus
from sqlalchemy.exc import SQLAlchemyError
from flask import request, abort
from src.schemas.session_exercises.session_ex_create import SessionExercisesCreationModel
from src.repository.session import get_sessions_by_filters
from src.repository import session as session_repository

class SessionExercisesByIdApi(Resource):

    def post(self, session_id: int) -> dict:
        try:
            if not session_repository.get_sessions_by_filters(session_filters={'session_id': session_id}).scalar():
                raise SessionNotFound(details=f"Session with id: {session_id} not found.")
            data: dict = request.get_json()
            session_exercises: SessionExercisesCreationModel = SessionExercisesCreationModel(**data).session_exercises
            new_session_exercises = [SessionExercise(session_id=session_id, **session_exercise.model_dump()) for session_exercise in session_exercises]
            session_exercise_repository.create_session_exercises(new_session_exercises)

            return [SessionExerciseResponseModel.model_validate(session_exercise).model_dump(by_alias=True) for session_exercise in new_session_exercises]

        except SessionNotFound as exc:
            abort(HTTPStatus.NOT_FOUND, description=str(exc.details))
        except (SQLAlchemyError, ValueError) as exc:
            abort(HTTPStatus.INTERNAL_SERVER_ERROR, description=exc)

    def get(self, session_id: int) -> list[dict]:
        session_exercises: list[SessionExercise] = session_exercise_repository \
        .get_session_exercises_by_filters({'session_id': session_id}).all()

        return [SessionExerciseResponseModel.model_validate(session_exercise).model_dump()
                for session_exercise in session_exercises]