from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from uuid import uuid4
from datetime import datetime

class Attendance(Base):
    __tablename__ = "attendancerecords"
    id = Column(Integer, primary_key=True, index=True, default=lambda: str(uuid4()))
    student_id = Column(String, ForeignKey("students.id"), unique=True, nullable=True)
    teacher_id = Column(String, ForeignKey("teachers.id"), unique=True, nullable=True)
    check_in_time = Column(datetime, nullable=True)
    check_out_time = Column(datetime, nullable=True)
    is_late = Column(String, default="No", nullable=True)
    left_early = Column(String, default="No", nullable=True)

student = relationship("Student", back_populates="Attendance")
teachers = relationship("Teacher", back_populates="Attendance")