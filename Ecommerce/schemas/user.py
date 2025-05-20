from pydantic import BaseModel

class UserCreate(BaseModel):
    full_name: str = None
    username: str
    email: str
    password: str

class UserLogin(BaseModel):
    email: str
    password: str