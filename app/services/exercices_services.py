from app.repository.exercices_repository import ExercicesRepository


class ExercicesService:
    def __init__(self):
        self.exercise_repo = ExercicesRepository()

    def get_all_exercises(self):
        return self.exercise_repo.get_all_exercises()

    def get_exercise_by_id(self, exercise_id):
        return self.exercise_repo.get_exercise_by_id(exercise_id)
