from http import HTTPStatus

from flask_restful import Resource
from sqlalchemy.exc import SQLAlchemyError
from flask import request, abort

from src.db.models.session import Session
from src.db.models.session_exercise import SessionExercise
from src.schemas.session_exercises.session_ex_create import SessionExerciseCreationModel
from src.schemas.session_exercises.session_ex_response import SessionExerciseResponseModel

from factory import session

class SessionExercisesApi(Resource):
    def post(self) -> dict:
        try:
            data: dict = request.get_json()
            session_ex_creation_model: SessionExerciseCreationModel = SessionExerciseCreationModel(**data)

            new_session_ex = SessionExercise(**session_ex_creation_model.model_dump())
            session.add(new_session_ex)
            session.commit()

            return SessionExerciseResponseModel.model_validate(new_session_ex).model_dump()

        except SQLAlchemyError as exc:
            abort(HTTPStatus.INTERNAL_SERVER_ERROR, description=exc)

    #
    # def get(self) -> str:
    #     try:
    #         # data: dict = request.get_json()
    #         # hero_filters: HeroFiltersModel = HeroFiltersModel(**data)
    #
    #         # return [hero.model_dump() for hero in get_heroes_by_filters(hero_filters=hero_filters)]
    #         return "gGggagaggagaga"
    #
    #     except SQLAlchemyError as exc:
    #         abort(HTTPStatus.INTERNAL_SERVER_ERROR, description=exc)