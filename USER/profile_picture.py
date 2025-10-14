from fastapi import File, UploadFile, HTTPException, status,Depends
from fastapi.responses import FileResponse
import shutil
import os
from sqlalchemy.orm import Session
from USER import user_models
from user_models import User
from database import get_db
from auth.dependencies import get_current_user



#User should be able to upload a profile picture
UPLOAD_FOLDER = "PROFILE_PICTURES"
os.path.exists(UPLOAD_FOLDER, exists_ok=True)

ALLOWED_EXTENSIONS = {"jpeg", "jpg", "png", "webg"}
def is_file_allowed(filename: str):
    return filename.split('.')[-1].lower() in ALLOWED_EXTENSIONS

def upload_profile_picture(current_user: User = Depends(get_current_user), 
                        file: UploadFile = File(...), db: Session = Depends(get_db)):
    
    if not current_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail= "Sorry, you don't have access to upload a picture here.")
    if not is_file_allowed(file.filename):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="File not accepted. Pleas upload a valid image.")
    file_extension = file.filename.split('.')[-1]
    file_name = f"profile_{current_user.full_name}.{file_extension}"
    file_path = os.path.join(UPLOAD_FOLDER, file_name)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    user = db.query(user_models.User).filter(user_models.User.id==current_user.id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail="User not found.")

    db.commit()
    db.refresh(user)
    return {"message": "Profile picture uploaded successfully.", "file_path": user.profile_picture_url}


def get_profile_picture(filename: str):
    file_extension = filename
    file_path = os.path.join(UPLOAD_FOLDER, file_extension)
    if not os.path.exists(file_path):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = "File not found.")
    return FileResponse({"file_path": file_path})

def update_profile_picture(current_user: User = Depends(get_current_user), 
            db: Session = Depends(get_db), file: UploadFile = File(...), old_picture: str):
    file_extension = file.filename.split('.')[-1] 
    file_path = f"profile_{current_user.full_name}.{file_extension}"
    old_picture = os.path.join(UPLOAD_FOLDER, file_path)
    new_picture = os.path.join(UPLOAD_FOLDER, file_path)
    
    picture = os.replace(old_picture, new_picture)
    db.commit()
    db.refresh(picture)
    return {"meesage": "File updated successfully.", "file_path": file_path}
