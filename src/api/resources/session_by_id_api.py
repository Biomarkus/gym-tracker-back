from http import HTTPStatus

from flask import abort, request
from flask_restful import Resource
from sqlalchemy.exc import SQLAlchemyError

from factory import session
from src.db.models.session import Session
from src.db.models.session_exercise import SessionExercise
from src.db.models.session_tag import SessionTag
from src.exceptions.session_exceptions import SessionNotFound
from src.exceptions.tag_exceptions import TagNotFound
from src.repository import session as session_repository
from src.schemas.session_exercises.session_ex_create import SessionExerciseBasicModel
from src.schemas.sessions.session_response import SessionResponseModel
from src.schemas.sessions.session_update import SessionUpdateModel
from src.repository import session_tags as session_tags_repository
from src.repository import session_exercise as session_exercise_repository


def get_session_or_abort(session_id: int) -> Session:
    session_by_id = (session_repository.
                     get_sessions_by_filters(session_filters={'session_id': session_id}).scalar())
    if not session_by_id:
        raise SessionNotFound(details=f"Session with id: {session_id} not found.")
    return session_by_id


def get_session_tags(tag_ids: list[int]) -> list[SessionTag]:
    new_tags: list[SessionTag] = []
    for tag_id in tag_ids:
        tag = session_tags_repository.get_session_tags_by_filters(session_tags_filters={'tag_id': tag_id}).scalar()
        if not tag:
            raise TagNotFound(details=f"Tag with id: {tag_id} not found.")
        new_tags.append(tag)

    return new_tags

def update_session_exercises(session_id: int, session_exercises: list[SessionExerciseBasicModel]) -> None:
    session_exercise_repository.delete_session_exercises(session_id)
    session_exercise_repository.create_session_exercises([SessionExercise(session_id=session_id,
                                                                          **session_exercise.model_dump())
                                                          for session_exercise in session_exercises])

class SessionByIdApi(Resource):

    def get(self, session_id: int) -> dict:
        try:
            session_by_id = get_session_or_abort(session_id)

            return SessionResponseModel.model_validate(session_by_id).model_dump(by_alias=True)
        except SessionNotFound as exc:
            abort(HTTPStatus.NOT_FOUND, description=str(exc.details))
        except SQLAlchemyError as exc:
            abort(HTTPStatus.INTERNAL_SERVER_ERROR, description=str(exc))

    def put(self, session_id: int) -> list[dict]:
        try:
            data = request.get_json()
            updated_session = SessionUpdateModel(**data)
            session_to_update = get_session_or_abort(session_id)
            if updated_session.title:
                session_to_update.title = updated_session.title
            if updated_session.end_date:
                session_to_update.end_date = updated_session.end_date
            if updated_session.session_tag_ids:
                session_to_update.session_tags = get_session_tags(updated_session.session_tag_ids)
            if updated_session.session_exercises:
                update_session_exercises(session_id, updated_session.session_exercises)

            session.commit()
            session.refresh(session_to_update)

            return SessionResponseModel.model_validate(session_to_update).model_dump()
        except (SessionNotFound, TagNotFound) as exc:
            abort(HTTPStatus.NOT_FOUND, description=exc.details)
        except SQLAlchemyError as exc:
            abort(HTTPStatus.INTERNAL_SERVER_ERROR, description=str(exc))


