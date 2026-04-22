from flask import request
from flask_restful import Resource

from models.exercise import Exercise
from src.repository.exercise import create_multiple_exercises
from src.schemas.exercises.exercise_response import ExerciseResponseModel
from src.schemas.exercises_multipe.exercises_multiple_create import ExercisesCreationModel
from src.schemas.exercises_multipe.exercises_multiple_response import ExercisesResponseModel


class ExercisesApiMultiple(Resource):
    def post(self) -> list[dict]:
        data: dict = request.get_json()
        exercises = ExercisesCreationModel(**data).exercises

        new_exercises = [Exercise(**exercise.model_dump()) for exercise in exercises]

        create_multiple_exercises(new_exercises)

        response_exercises = [ExerciseResponseModel.model_validate(exercise) for exercise in new_exercises]
        return ExercisesResponseModel(exercises=response_exercises).model_dump()

