from sqlalchemy.orm import Session
from app.database import get_db
from USER.user_models import User
from USER.user_schemas import UserCreate, UserLogin
from auth.hashing import password_hash, password_verify
from fastapi import HTTPException, status




def create_user(db: Session, user: UserCreate, user_id: int):
    hashed_password = password_hash(user.password)
    existing_users = db.query(User).filter(User.id==user_id).first()
    if existing_users:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="This account already exist.")
    new_user = User(
        username = user.username,
        full_name = user.full_name,
        email = user.email,
        hashed_password = hashed_password,
        role = user.role,
        country = user.country,
        gender = user.gender

    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return{"message": "Account created successsfully."}

def get_user_by_id(user_id: str, db: Session):
    user = db.query(User).filter(User.id==user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = "File not found.")
    return user

def user_by_email(email: str, db: Session):
    user = db.query(User).filter(User.email==email).filter()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found.")
    return user


def update_user(user_id: str, update_data: UserCreate, db: Session):
    users = db.query(User).filter(User.id==user_id).first()
    if not users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    
    update_users = User(
        username = update_data.username,
        full_name = update_data.full_name,
        password = update_data.password,
        country = update_data.country,
        role = update_data.role,
        email = update_data.email,
        gender = update_data.gender
    )
    db.commit()
    db.refresh(update_users)
    return update_users 