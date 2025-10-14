from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ATTENDANCE import attendance_schemas, attendance_crud, attendance_models
from auth.dependencies import get_current_user
from database import get_db
from attendance_models import Attendance
from USER.user_models import User

router = APIRouter(prefix = "/attendance-log",
                   tags= ["Attendance"])

@router.post("/sign_in")
def sign_in(user_id: str, check_in_time: str, current_user:User=Depends(get_current_user), db: Session=Depends(get_db)):
    return attendance_crud.sign_in(user_id=user_id, current_user=current_user, db=db, check_in_time=check_in_time)


@router.post("sign_out")
def sign_out(user_id: str, check_out_time: str, current_user: User=Depends(get_current_user), db: Session=Depends(get_db)):
    return attendance_crud.sign_out(user_id=user_id, check_out_time=check_out_time, current_user=current_user, db=db)

@router.post("/lateness")
def lateness(user_id: str, db: Session=Depends(get_db), currecnt_user: User=Depends(get_current_user)):
    return attendance_crud.lateness(user_id=user_id, db=db, currecnt_user=currecnt_user)

@router.post("/early")
def early(user_id: str, db: Session=Depends(get_db), current_user: User = Depends(get_current_user)):
return attendance_crud.