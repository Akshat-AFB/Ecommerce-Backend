from repositories.user_repo import UserRepository

class UserService:
    @staticmethod
    def register(email: str, password: str, full_name: str, username: str):
        if UserRepository.get_user(email):
            raise Exception("User Already Exists")
        return UserRepository.create_user(email, password, full_name, username)

    @staticmethod
    def login(email: str, password: str):
        user = UserRepository.get_user(email)
        if user and user["password"] == password:
            return True
        return False