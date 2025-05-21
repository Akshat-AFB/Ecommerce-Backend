from pydantic import BaseModel

class User(BaseModel):
    full_name: str = None
    username: str
    email: str
    password: str

class UserInDB(User):
    hashed_password: str