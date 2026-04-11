from http import HTTPStatus

from flask_restful import Resource
from sqlalchemy.exc import SQLAlchemyError
from flask import request, abort

from src.db.models.session import Session
from src.schemas.sessions.session_create import SessionCreationBasicModel
from factory import session

class SessionExercisesApi(Resource):
    def post(self) -> dict:
        try:
            data: dict = request.get_json()
            hero_creation_model: SessionCreationBasicModel = SessionCreationBasicModel(**data)

            new_session = Session(**hero_creation_model.model_dump())
            session.add(new_session)
            session.commit()


            return new_session.model_dump()

        except SQLAlchemyError as exc:
            abort(HTTPStatus.INTERNAL_SERVER_ERROR, description=exc)


    def get(self) -> str:
        try:
            # data: dict = request.get_json()
            # hero_filters: HeroFiltersModel = HeroFiltersModel(**data)

            # return [hero.model_dump() for hero in get_heroes_by_filters(hero_filters=hero_filters)]
            return "gGggagaggagaga"

        except SQLAlchemyError as exc:
            abort(HTTPStatus.INTERNAL_SERVER_ERROR, description=exc)