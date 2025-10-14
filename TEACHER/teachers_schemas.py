from pydantic import BaseModel

class TeacherBase(BaseModel):
    front_id_card_url: str
    back_id_card_url: str

class TeacherCreate(TeacherBase):
    pass

class TeacherResponse(TeacherCreate):
    id: str
    teacher_id: str

class Config:
    orm_mode = True

