import json
from app.data import users_file_path

class UserRepository:
    def __init__(self):
        self.file_path = users_file_path

    def _read_data(self):
        with open(self.file_path, "r") as file:
            return json.load(file)

    def _write_data(self, data):
        with open(self.file_path, "w") as file:
            json.dump(data, file, indent=4)

    def get_all_users(self):
        return self._read_data()

    def get_user_by_id(self, user_id):
        users = self._read_data()
        return next((user for user in users if user["id"] == user_id), None)

    def add_user(self, user):
        users = self._read_data()
        users.append(user)
        self._write_data(users)

    def update_user(self, user_id, updated_user):
        users = self._read_data()
        for index, user in enumerate(users):
            if user["id"] == user_id:
                users[index] = updated_user
                break
        self._write_data(users)

    def delete_user(self, user_id):
        users = self._read_data()
        users = [user for user in users if user["id"] != user_id]
        self._write_data(users)
