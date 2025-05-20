from Ecommerce.repositories.user_repo import UserRepository

class UserService:
    @staticmethod
    def register(email: str, password: str):
        return UserRepository.create_user(email, password)

    @staticmethod
    def login(email: str, password: str):
        user = UserRepository.get_user(email)
        if user and user["password"] == password:
            return True
        return False