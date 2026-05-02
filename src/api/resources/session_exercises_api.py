from http import HTTPStatus

from flask_restful import Resource
from pydantic import ValidationError
from sqlalchemy.exc import SQLAlchemyError
from flask import request, abort

from src.db.models.session_exercise import SessionExercise
from src.schemas.session_exercises.session_ex_create import SessionExerciseCreationModel
from src.schemas.session_exercises.session_ex_response import SessionExerciseResponseModel
from src.repository import session_exercise as session_exercise_repository
from factory import session

class SessionExercisesApi(Resource):
    def post(self) -> dict:
        try:
            data: dict = request.get_json()
            session_ex_creation_model: SessionExerciseCreationModel = SessionExerciseCreationModel(**data)
            new_session_ex = SessionExercise(**session_ex_creation_model.model_dump())
            session_exercise_repository.create_session_exercise(new_session_ex)

            return SessionExerciseResponseModel.model_validate(new_session_ex).model_dump()

        except SQLAlchemyError as exc:
            abort(HTTPStatus.INTERNAL_SERVER_ERROR, description=exc)
