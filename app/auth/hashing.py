from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def password_hash(password: str):
    return pwd_context.hash(password)

def password_verify(plain_password: str, password:str):
    return pwd_context.verify(plain_password, password)
