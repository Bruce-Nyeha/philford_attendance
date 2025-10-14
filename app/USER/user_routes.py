from fastapi import APIRouter, HTTPException, Depends, status
from USER import user_crud, user_models, user_schemas
from sqlalchemy.orm import Session
from database import get_db
from user_crud import UserCreate
from auth.dependencies import get_current_user
from user_models import User
from USER.profile_picture import upload_profile_picture, update_profile_picture,get_profile_picture

router = APIRouter(
    prefix="/regiter-user",
    tags=["Registration"]
)

@router.post("/register")
def register_user(db: Session = Depends(get_db), user: UserCreate = Depends()):
    users = user_crud.create_user(db=db, user=user)
    return users

@router.post("/upload-profile-picture")
def upload_profile_picture(db: Session=Depends(get_db), current_user: User = Depends(get_current_user),
                           user=user_schemas.UserCreate):
    user.profile_picture_url = upload_profile_picture (db=db, current_user=current_user)
    return user

@router.get("/get-profile-picture")
def get_profile_picture(filename: str):
    picture = get_profile_picture(filename=filename)
    return picture

@router.put("/update-profile")
def update_profile(db: Session=Depends(get_current_user)):
    picture = update_profile(db=db)
    return picture
