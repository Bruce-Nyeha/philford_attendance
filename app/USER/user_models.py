from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from uuid import uuid4
from datetime import datetime
from app.enums import UserRole
from app.database import Base
from app.enums import UserRole,Gender

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True, default=lambda: str(uuid4()))
    username = Column(String, unique=True, nullable=False)
    full_name = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    country = Column(String, nullable=True)
    role = Column(UserRole, default=UserRole.student, nullable=True)
    gender = Column(Gender, nullable=True)
    email = Column(String, unique=True, nullable=False)
    profile_picture_url = Column(String, nullable=True)
    created_at = Column(default=datetime.utcnow)

student = relationship("Student", back_populates="user", uselist=False)
teacher = relationship("Teacher", back_populates="teachers", uselist=False)