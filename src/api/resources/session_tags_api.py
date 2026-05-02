from http import HTTPStatus

from flask import request
from flask_restful import Resource, abort
from sqlalchemy.exc import SQLAlchemyError

from src.db.models.session_tag import SessionTag
from src.exceptions.tag_exceptions import TagConflict
from src.repository import session_tags as session_tags_repository
from src.schemas.session_tags.session_tags_create import SessionTagsCreationModel
from src.schemas.session_tags.session_tags_response import SessionTagResponseModel


class SessionTagsApi(Resource):
    def post(self) -> list[dict]:
        try:
            data: dict = request.get_json()
            tags_creation_models: SessionTagsCreationModel = SessionTagsCreationModel(**data)
            new_tags: list[SessionTag] = []
            for tag_name in tags_creation_models.tag_names:
                if session_tags_repository.get_session_tags_by_filters(session_tags_filters={'name': tag_name}).scalar():
                    raise TagConflict(details=f"Tag with name: {tag_name} already exists!")
                new_tags.append(SessionTag(name=tag_name))
            session_tags_repository.create_new_tags(new_tags)

            return [SessionTagResponseModel.model_validate(new_tag).model_dump() for new_tag in new_tags]
        except TagConflict as e:
            abort(HTTPStatus.CONFLICT, description=e.details)
        except SQLAlchemyError as e:
            abort(HTTPStatus.INTERNAL_SERVER_ERROR, description=str(e))

    def get(self) -> list[dict]:
        tags = session_tags_repository.get_session_tags_by_filters(session_tags_filters={}).all()

        return [SessionTagResponseModel.model_validate(tag).model_dump() for tag in tags]

