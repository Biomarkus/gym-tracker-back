from pydantic import BaseModel


class SessionExerciseCreationModel(BaseModel):
    session_id: int
    exercise_id: int
    reps: int
    weight: int