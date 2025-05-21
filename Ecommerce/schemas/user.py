from pydantic import BaseModel

class UserCreate(BaseModel):
    user_id: str = None
    full_name: str
    username: str
    email: str
    password: str
    

class UserLogin(BaseModel):
    email: str
    password: str