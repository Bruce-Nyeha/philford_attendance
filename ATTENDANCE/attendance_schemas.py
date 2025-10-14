from pydantic import BaseModel
from typing import Optional
import datetime

class AttendanceBase(BaseModel):
    chech_in_time: datetime 
    chech_out_time: datetime

class AttendanceCreate(AttendanceBase):
    is_late: str
    left_ealry: str


class AttendanceResponse(AttendanceBase):
    id: str
    student_id: str
    teacher_id: str


class Config:
    orm_mode=True

