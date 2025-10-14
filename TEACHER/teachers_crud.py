from USER.user_models import User
from auth.dependencies import get_current_user
from database import get_db
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status
#this function is to check if the user is a teacher if not we raise an error if yes then we should be able to get the user
def get_teacher(user_id: str, db: Session, current_user: User = Depends(get_current_user)):
    teachers = db.query(User).filter(User.id==user_id).first()
    if teachers.role != teachers:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail= "Sorry, you don't have access here.")
    if not teachers:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User or teacher not found.")
    return teachers
