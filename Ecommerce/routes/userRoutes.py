from fastapi import APIRouter, status, HTTPException
from schemas.user import UserCreate, UserLogin
from services.userService import UserService
router = APIRouter()

@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register_user(user: UserCreate):
    try:
        UserService.register(user.email, user.password, user.full_name, user.username)
        return {"message": "User registered successfully", "user": user}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    
@router.post("/login", status_code = status.HTTP_200_OK)
async def login(user: UserLogin):
    try:
        UserService.login(user.email, user.password)
        return {"message": "User Logged in Successfully", "user": user}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail = " Wrong Credentials ")