from app.repository.user_repository import UserRepository


class UserService:
    def __init__(self):
        self.user_repo = UserRepository()

    def get_all_users(self):
        return self.user_repo.get_all_users()

    def get_user_by_id(self, user_id):
        return self.user_repo.get_user_by_id(user_id)

    def create_user(self, user_data):

        self.user_repo.add_user(user_data)
        return user_data

    def update_user(self, user_id, updated_user_data):
        user = self.user_repo.get_user_by_id(user_id)
        if user:
            updated_user_data["id"] = user_id
            self.user_repo.update_user(user_id, updated_user_data)
            return updated_user_data
        return None

    def delete_user(self, user_id):
        self.user_repo.delete_user(user_id)
