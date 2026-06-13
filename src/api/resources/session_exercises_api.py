from http import HTTPStatus

from flask_restful import Resource
from pydantic import ValidationError
from sqlalchemy.exc import SQLAlchemyError
from flask import request, abort

from src.db.models.session_exercise import SessionExercise
from src.schemas.session_exercises.session_ex_create import SessionExerciseCreationModel, SessionExercisesCreationModel
from src.schemas.session_exercises.session_ex_response import SessionExerciseResponseModel
from src.repository import session_exercise as session_exercise_repository

class SessionExercisesApi(Resource):
    def post(self) -> dict:
        try:
            data: dict = request.get_json()
            session_exercises: SessionExercisesCreationModel = SessionExercisesCreationModel(**data).session_exercises
            new_session_exercises = [SessionExercise(**session_exercise.model_dump()) for session_exercise in session_exercises]
            session_exercise_repository.create_session_exercises(new_session_exercises)

            return [SessionExerciseResponseModel.model_validate(session_exercise).model_dump(by_alias=True) for session_exercise in new_session_exercises]

        except SQLAlchemyError as exc:
            abort(HTTPStatus.INTERNAL_SERVER_ERROR, description=exc)
