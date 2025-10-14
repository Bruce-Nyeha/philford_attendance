from fastapi import HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer
from auth.token import verify_acess_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")
# now we creating our function to get current user or making this our dependencies.
# This helps to protect our routes

def get_current_user(token: str= Depends(oauth2_scheme)):
     credentials_exception = HTTPException(
     status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Invalid or expired credentials.",
    headers={"WWW-Authenticate": "Bearer"})
     return verify_acess_token(token, credentials_exception)