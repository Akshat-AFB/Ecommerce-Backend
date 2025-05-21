from authentication.auth import hash_password, verify_password, create_access_token
from repositories.user_repo import UserRepository # your in-memory or DB repo
from schemas.token import TokenResponse

class UserService:
    @staticmethod
    def register(email, password, full_name, username):
        if UserRepository.get_user(email):
            raise Exception("Email already exists")
        hashed = hash_password(password)
        UserRepository.create_user(email, hashed, full_name, username)

    @staticmethod
    def login(email, password) -> TokenResponse:
        user = UserRepository.get_user(email)
        print(email)
        print(user)
        print(user["password"])
        print(password)
        # hashed = hash_password(password)
        print(verify_password(password, user["password"]))
        if not user or not verify_password(password, user["password"]):
            raise Exception("Invalid credentials")
        
        token = create_access_token({"sub": user["email"]})
        return TokenResponse(access_token=token)


# from repositories.user_repo import UserRepositorysitory
# from fastapi.security import OAuth2PasswordRequestForm
# from models.user import User, UserInDB
# from models.token import Token
# from authentication.auth import hash_password, verify_password, create_access_token
# from fastapi import HTTPException

# class UserService:
#     @staticmethod
#     def register(email: str, password: str, full_name: str, username: str):
#         if UserRepositorysitory.get_user(email):
#             raise Exception("User Already Exists")
#         hashed = hash_password(password)
#         user = {"email": email, "password": hashed, "full_name": full_name, "username": username}
#         user_in_db = UserInDB(**user.dict(), hashed_password=hashed)
#         UserRepositorysitory.create_user(user_in_db)
#         token = create_access_token({"sub": email})
#         return Token(access_token=token, token_type="bearer")

#     def login_user(form_data: OAuth2PasswordRequestForm) -> Token:
#         user = UserRepositorysitory.get_user_by_username(form_data.email)
#         if not user or not verify_password(form_data.password, user.hashed_password):
#             raise HTTPException(status_code=401, detail="Invalid username or password")
        
#         token = create_access_token({"sub": user.username})
#         return Token(access_token=token, token_type="bearer")
#     # @staticmethod
#     # def login(email: str, password: str):
#     #     user = UserRepositorysitory.get_user(email)
#     #     if user and user["password"] == password:
#     #         return True
#     #     return False
    
#     @staticmethod
#     def is_logged_in(user_id: str) -> bool:
#         return UserRepositorysitory.is_logged_in(user_id)