from fastapi import APIRouter, Depends,HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.auth import token, hashing, auth_crud
from app.database import get_db

router = APIRouter(
    prefix="/auth", tags=["Authentication"]
)

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = auth_crud.get_user_by_email(db, form_data.username)
    if not user or not hashing.password_verify(form_data.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials.")
    access_token = token.create_access_token(data={"user_id": user.id, "email": user.email, "role": user.role})
    return {"access_token": access_token, "token_type": "bearer"}