from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWSError, jwt

SECRET_KEY = "secret123"
ALGORITHM = "HS256"

oauth2_scheme = OAuth2PasswordBearer (tokenUrl="token")


def fake_decode_token (token):

    try:
        payload = jwt.decode (token, SECRET_KEY, algorithms= [ALGORITHM])
        username = payload.get ("sub")
        return {username}
    
    except JWSError:
        raise HTTPException (status_code=401, detail= "Invalid Token")
    

def get_current_user (token: str = Depends (oauth2_scheme)):
    return {fake_decode_token (token)}