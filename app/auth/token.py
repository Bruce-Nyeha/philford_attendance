from datetime import datetime, timedelta
from jose import JWTError, jwt
from app.config  import settings
from app.auth.auth_schemas import TokenData




#Creating of access token
SECRET_KEY = settings.SECRET_KEY
ALGORITHM = settings.ALGORITHM
ACESS_TOKEN_EXPIRE_MINUTES = settings.ACCESS_TOKEN_EXPIRE_MINUTES

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow + timedelta(minutes=ACESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=[ALGORITHM])
    return encoded_jwt

# now we then decode the token for verfiying the user access
def verify_acess_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("user_id")
        role: str = payload.get(role)
        if user_id is None or role is None:
            raise credentials_exception
        return TokenData(user_id = user_id, role = role)
    
    except JWTError:
        raise credentials_exception