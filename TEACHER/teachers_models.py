from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from uuid import uuid4

class Teacher(Base):
    __tablename__ = "teachers"
    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid4()))
    teacher_id = Column(String, ForeignKey("users.id"), index=True, nullable=True)
    front_id_card_url = Column(String, default=lambda:str(uuid4()))
    back_id_card_url = Column(String, default=lambda: str(uuid4()))

    user = relationship("User", back_populates="teachers", uselist=False)
    attendance = relationship("Attendance", back_populates="teachers", uselist=True)
    