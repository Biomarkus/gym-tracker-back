from http import HTTPStatus

from flask import request, abort
from flask_restful import Resource
from sqlalchemy.exc import SQLAlchemyError

from factory import session
from src.db.models.session import Session
from src.schemas.sessions.session_filters import SessionFiltersModel
from src.schemas.sessions.session_response import SessionResponseModel


class SessionFilterApi(Resource):
    def post(self) -> list[SessionResponseModel]:
        try:
            data: dict = request.get_json()
            session_filters: dict = SessionFiltersModel(**data).model_dump(exclude_none=True)

            result_query = session.query(Session)

            for field_name, value in session_filters.items():
                column = getattr(Session, field_name, None)
                if field_name == "title":
                    result_query = result_query.filter(column.like(f"%{value}%"))
                else:
                    result_query = result_query.filter(column == value)

            return [SessionResponseModel.model_validate(session_response).model_dump()
                    for session_response in result_query.all()]

        except SQLAlchemyError as exc:
            abort(HTTPStatus.INTERNAL_SERVER_ERROR, description=exc)