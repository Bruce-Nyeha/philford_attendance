from fastapi import APIRouter, HTTPException, Depends, UploadFile, File
from TEACHER import teachers_models, teachers_crud, teachers_schemas
from sqlalchemy.orm import Session
from database import get_db
from auth.dependencies import get_current_user
from TEACHER.teachers_models import Teacher
from TEACHER.teachers_crud import get_teacher

router = APIRouter(prefix = "/register-teacher",
                   tags = ["Teacher"])

@router.post("/teacher")
def get_teacher(user_id: str, db: Session = Depends(get_db), current_user: Teacher = Depends(get_current_user)):
    teacher = get_teacher(user_id=user_id, db=db, current_user=current_user)
    return teacher