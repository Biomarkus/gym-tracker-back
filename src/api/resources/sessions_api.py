from http import HTTPStatus

from flask_restful import Resource
from sqlalchemy.exc import SQLAlchemyError
from flask import request, abort

from factory import session
from src.db.models.session import Session
from src.db.models.session_exercise import SessionExercise
from src.db.models.exercise import Exercise
from src.db.models.category import Category
from src.schemas.sessions.session_create import SessionCreationBasicModel
from src.schemas.sessions.session_response import SessionResponseModel


class SessionsApi(Resource):
    def post(self) -> dict:
        try:
            data: dict = request.get_json()
            session_creation_model: SessionCreationBasicModel = SessionCreationBasicModel(**data)

            new_session = Session(**session_creation_model.model_dump())
            session.add(new_session)
            session.commit()


            return SessionResponseModel.model_validate(new_session).model_dump()

        except SQLAlchemyError as exc:
            abort(HTTPStatus.INTERNAL_SERVER_ERROR, description=exc)
