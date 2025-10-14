from sqlalchemy.orm import Session
from app.USER import user_models

def get_user_by_email(db: Session, email: str):
    user = db.query(user_models.User).filter(user_models.User.email==email).first()
    return user