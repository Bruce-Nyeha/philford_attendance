from sqlalchemy.orm import Session
from uuid import uuid4
from fastapi import HTTPException, status
from STUDENT.student_models import Student
from student_schemas import StudentCreate

def create_student(db: Session, student_data: StudentCreate, user_id: str):
    existing = db.query(Student).filter(Student.user_id==user_id).first()
    if existing:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Student already exist.")
    new_student = Student(
        id=str(uuid4()),
        age = student_data.age,
        parent_contact = student_data.parent_contact,
        passport_url = student_data.passport_url
    )
    db.commit()
    db.refresh(new_student)
    return new_student

def get_student_by_id(user_id: str, db: Session):
    student = db.query(Student).filter(Student.user_id==user_id).first()
    if not student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found.")
    return student

