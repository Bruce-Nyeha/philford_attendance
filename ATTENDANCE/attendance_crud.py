from sqlalchemy.orm import Session
from database import get_db
from auth.dependencies import get_current_user
from datetime import datetime, time
from ATTENDANCE.attendance_models import Attendance
from ATTENDANCE.attendance_schemas import AttendanceCreate
from USER.user_models import User
from fastapi import HTTPException, Depends, status
# I am going to create a function to check the time the student and teacher came in and left.
def sign_in(user_id: str, check_in_time: str, current_user: User = Depends(get_current_user), db: Session=Depends(get_db)):
    if current_user.role != "student" or current_user.role != "teacher":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Sorry, you don't have access here.")
    user = db.query(Attendance).filter(Attendance.id==user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found.")
    if user:
        check_in_time = datetime.utcnow

    user.check_in_time = check_in_time
    db.commit()
    db.refresh(user)

# I then create a function to check the time user signed-out
def sign_out(user_id: str, check_out_time: str, current_user: User=Depends(get_current_user), db: Session=Depends(get_db)):
    if current_user.role != "student" or current_user.role != "teacher":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Sorry, you don't have access here.")
    user = db.query(Attendance).filter(Attendance.id==user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found.")
    if user:
        check_out_time = datetime.utcnow

    user.check_out_time = check_out_time
    db.commit()
    db.refresh(user)


    # I then create a function to check if user is late for class.
def lateness(user_id: str, db: Session=Depends(get_db), currecnt_user: User=Depends(get_current_user)):
if current_user.role != "student" or current_user.role != "teacher":
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Sorry, you don't have access here.")
    user = db.query(Attendance).filter(Attendance.id==user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found.")
    late = time(9,0)
    late_ness = sign_in > late
    
Attendance.is_late = late_ness
db.commit()
db.refresh(user)
return {"message": "You came in late today."}

def early(user_id: str, db: Session=Depends(get_db), current_user: User = Depends(get_current_user)):
if current_user.role != "student" or current_user.role != "teacher":
          raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Sorry, you don't have access here.")
    user = db.query(Attendance).filter(Attendance.id==user_id).first()
    if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found.")
            left_early = time(13,0)
                early_leaving = sign_out < left_early 
    Attendance.left_early = early_leaving
                db.commit()
                db.refresh(user) 
                return{"message": "School hasn't closed yet."}