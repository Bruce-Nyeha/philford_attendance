from enums import Enum

class UserRole(str, Enum):
    student = "STUDENT"
    teacher = "TEACHER"
    admin = "ADMIN"


class Gender(str, Enum):
    male = "MALE"
    female = "FEMALE"
    