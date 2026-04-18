from http import HTTPStatus

from flask import request, abort
from flask_restful import Resource

from src.db.models.category import Category
from src.exceptions.category_exceptions import CategoryConflict
from src.repository.category import create_new_category
from src.schemas.categories.category_create import CategoryCreationModel

from src.repository import category as category_repository
from src.schemas.categories.category_response import CategoryResponseModel


class CategoriesApi(Resource):
    def post(self) -> dict:
        try:
            data: dict = request.get_json()
            category_creation_model: CategoryCreationModel = CategoryCreationModel(**data)
            if category_repository.get_categories_by_name(category_name=category_creation_model.name).scalar():
                raise CategoryConflict(details=f"Category with name: {category_creation_model.name} already exists!")
            create_new_category(category=Category(**category_creation_model.model_dump()))

            return CategoryResponseModel.model_validate(category_creation_model).model_dump()
        except CategoryConflict as e:
            abort(HTTPStatus.CONFLICT, description=e.details)

    def get(self) -> list[dict]:
        categories = category_repository.get_all_categories().all()

        return [CategoryResponseModel.model_validate(category).model_dump() for category in categories]
