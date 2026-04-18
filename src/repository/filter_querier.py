from typing import Any

from sqlalchemy.orm import Query, Session

class FilterQuerier:
    def __init__(self, session: Session, db_model: Any, filters: dict | None = None,
                 name_field: str | None = None) -> None:
        self._session = session
        self._model = db_model
        self._filters = filters
        self._name_search_field = name_field


    def filter_by_properties(self):
        result_query: Query = self._session.query(self._model)
        if not self._filters:
            return result_query

        for field_name, value in self._filters.items():
            column = getattr(self._model, field_name, None)
            if field_name == self._name_search_field:
                result_query = result_query.filter(column.like(f"%{value}%"))
            else:
                result_query = result_query.filter(column == value)

        return result_query

