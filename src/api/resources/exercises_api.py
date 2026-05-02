from flask import request
from flask_restful import Resource

from src.db.models.exercise import Exercise
from src.exceptions.exercise_exceptions import ExerciseConflict
from src.repository import exercise as exercise_repository
from src.repository.exercise import create_new_exercise
from src.schemas.exercises.exercise_create import ExerciseCreationModel
from src.schemas.exercises.exercise_response import ExerciseResponseModel


class ExercisesApi(Resource):
    def post(self) -> dict:
        data: dict = request.get_json()
        exercise_creation_model: ExerciseCreationModel = ExerciseCreationModel(**data)
        if exercise_repository.get_exercise_by_filters({'title': exercise_creation_model.title,
                                                        'category_id': exercise_creation_model.category_id}).scalar():
            raise ExerciseConflict(details=f"Exercise with this name and category id already exists")
        new_exercise = Exercise(**exercise_creation_model.model_dump())
        create_new_exercise(new_exercise)

        return ExerciseResponseModel.model_validate(new_exercise).model_dump()

    def get(self) -> list[dict]:
        exercises = exercise_repository.get_exercise_by_filters().all()

        return [ExerciseResponseModel.model_validate(exercise).model_dump() for exercise in exercises]



