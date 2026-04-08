from http import HTTPStatus

from flask_restful import Resource
from sqlalchemy.exc import SQLAlchemyError
from flask import request, abort


class SessionsApi(Resource):
    # def post(self) -> dict:
    #     try:
    #         data: dict = request.get_json()
    #         hero_creation_model: HeroCreationModel = HeroCreationModel(**data)
    #
    #         new_hero = create_hero(hero_creation_model=HeroCreationBasicModel(**hero_creation_model.model_dump()),
    #                                powers=hero_creation_model.powers)
    #
    #         socket.emit("new_hero", {'hero_id': new_hero.hero_id, "hero_data": new_hero.model_dump()})
    #
    #         return new_hero.model_dump()
    #
    #     except HeroConflict:
    #         abort(HTTPStatus.CONFLICT, description=f"Hero with this name already exists!")
    #     except SQLAlchemyError as exc:
    #         abort(HTTPStatus.INTERNAL_SERVER_ERROR, description=exc)


    def get(self) -> str:
        try:
            # data: dict = request.get_json()
            # hero_filters: HeroFiltersModel = HeroFiltersModel(**data)

            # return [hero.model_dump() for hero in get_heroes_by_filters(hero_filters=hero_filters)]
            return "gGggagaggagaga"

        except SQLAlchemyError as exc:
            abort(HTTPStatus.INTERNAL_SERVER_ERROR, description=exc)