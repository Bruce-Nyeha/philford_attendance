from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from STUDENT import student_models, student_crud, student_schemas
from database import get_db
from auth.dependencies import get_current_user
from student_models import Student

router = APIRouter(prefix = "/register-student",
    tags=["Student"])
    

@router.post("/student")
def create_student(user_id: str, db: Session = Depends(get_db), current_user: Student = Depends(get_current_user)):
    existing_student = db.query(Student).filter(Student.user_id==user_id).first()
    if existing_student:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Sorry, student already exist.")
    return student_crud.create_student 
{"message": " Successfully created."}

@router.get("get_user_by_id")
def student_by_id(db: Session= Depends(get_db)):
    return student_crud.get_student_by_id

