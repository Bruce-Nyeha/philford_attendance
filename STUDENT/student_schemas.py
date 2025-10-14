from pydantic import BaseModel


class StudentBase(BaseModel):
    age: str
    passport_url: str
    parent_contact: str
class StudentCreate(StudentBase):
        pass

class StudentResponse(StudentBase):
    id: str
    user_id: str

class Config:
    orm_mode=True

