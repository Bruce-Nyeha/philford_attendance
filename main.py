
from fastapi import FastAPI
from database import engine, Base
from auth import auth_routes
from USER import user_models, user_routes
from config import settings
from STUDENT import student_routes, student_models
from ATTENDANCE import attendance_models


user_models.Base.metadata.create_all(bind=engine)
student_models.Base.metadata.create_all(bind=engine)
attendance_models.Base.metadata.create_all(bind=engine)

apps = FastAPI(title="Philford Attendance API")

apps.include_router(auth_routes.router, prefix="/auth", tags=["Auth"])
apps.include_router(user_routes.router, prefix="/register-user", tags=["Registration"])
apps.include_router(student_routes.router, prefix="/student-user", tags=["Student"])
