
from fastapi import File, UploadFile, HTTPException, status, Depends
from fastapi.responses import FileResponse
from TEACHER.teachers_models import Teacher
from sqlalchemy.orm import Session
from auth.dependencies import get_current_user
from database import get_db
from USER.user_models import User
from datetime import datetime
import os
import shutil

#we then create the file upload to handle the front and back of the id card...
UPLOAD_FOLDER = "ID_CARD_FOLDER"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

EXTENSION = ["png", "jpeg", "jpg"]
#we define a function to accepts this required file extention
def allowed_extension(filename: str):
    file_extension = filename.split('.')[-1].lower()
    if file_extension not in EXTENSION:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Sorry, check your file extension.")
    return file_extension

def front_id_card(user_id: str, db: Session, file: UploadFile = File(...), current_user: User = Depends(get_current_user)):
    teachers = db.query(Teacher).filter(Teacher.id==user_id).first()
    if current_user.role != teachers:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Sorry, you can't upload a picture here.")
    extension = allowed_extension()
    file_name = f"{current_user.full_name}_{datetime.utcnow().strftime('%Y%m%d%H%M%S')}.{extension}"
    file_path = os.path.join(UPLOAD_FOLDER, file_name)
    
    if os.path.exists(file_path):
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
    teachers.front_id_card_url = file_path
    
    db.commit()
    db.refresh(teachers)        
    return {"message": "image uploaded successfully.", "file_path": file_path}


#Teacher should br able to view file upload

def back_id_card(user_id: str, db: Session, file: UploadFile = File(...), current_user: User = Depends(get_current_user)):
    teachers = db.query(Teacher).filter(Teacher.id==user_id).first()
    if current_user.role != teachers:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Sorry, you can't upload a picture here.")
    extension = allowed_extension()
    file_name = f"{current_user.full_name}_{datetime.utcnow().strftime('%Y%m%d%H%M%S')}.{extension}"
    file_path = os.path.join(UPLOAD_FOLDER, file_name)
    
    if os.path.exists(file_path):
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
    teachers.back_id_card_url = file_path
    db.commit()
    db.refresh(teachers)
    return {"message": "image uploaded successfully.", "file_path": file_path}
