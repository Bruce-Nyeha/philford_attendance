from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from uuid import uuid4
from database import Base
class Student(Base):
    __tablename__ = "students"
    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid4()))
    user_id = Column(String, ForeignKey("users.id"), unique=True, nullable=True)
    age = Column(Integer, nullable=True)
    parent_contact = Column(String, nullable=True)
    passport_url = Column(String, nullable=True)

    user = relationship("User", back_populates="student")
    attendance = relationship("Attendance", back_populates="students", uselist=True)
    