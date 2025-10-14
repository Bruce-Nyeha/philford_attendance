from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime
from enums import UserRole,Gender
class UserBase(BaseModel):
    username: str
    full_name: str
    country: str
    gender: Gender
    email: EmailStr
    profile_picture_url: Optional[str]  
    role: UserRole

class UserCreate(UserBase):
    password: str

class UserOut(UserBase):
    id: int
    created_at: datetime

class Config:
    orm_mode=True

class UserLogin(BaseModel):
    username: str
    password: str
