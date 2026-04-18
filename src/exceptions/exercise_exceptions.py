from src.exceptions import BasicException


class ExerciseConflict(BasicException):
    def __init__(self, details: str):
        super().__init__(409, details)