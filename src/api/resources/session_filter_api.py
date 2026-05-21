from http import HTTPStatus

from flask import request, abort
from flask_restful import Resource
from sqlalchemy.exc import SQLAlchemyError

from factory import session
from src.repository.session import get_sessions_by_filters
from src.schemas.sessions.session_filters import SessionFiltersModel
from src.schemas.sessions.session_response import SessionResponseModel


class SessionFilterApi(Resource):
    def post(self) -> list[SessionResponseModel]:
        try:
            data: dict = request.get_json()
            session_filters: dict = SessionFiltersModel(**data).model_dump(exclude_none=True)

            sessions_query = get_sessions_by_filters(session_filters=session_filters)

            return [SessionResponseModel.model_validate(session_response).model_dump(by_alias=True)
                    for session_response in sessions_query.all()]

        except SQLAlchemyError as exc:
            abort(HTTPStatus.INTERNAL_SERVER_ERROR, description=exc)