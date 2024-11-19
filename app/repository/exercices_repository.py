import json
from app.data import exercices_file_path


class ExercicesRepository:
    def __init__(self):
        self.file_path = exercices_file_path

    def _read_data(self):
        with open(self.file_path, "r") as file:
            return json.load(file)

    def get_all_exercises(self):
        return self._read_data()

    def get_exercise_by_id(self, exercise_id):
        exercices = dict(self._read_data())
        exercise_found = exercices.get(exercise_id)
        print("encontrado en el repo", exercise_found)
        return exercise_found
