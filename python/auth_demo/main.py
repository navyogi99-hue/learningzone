from fastapi import FastAPI 
from fastapi import FastAPI, Depends, HTTPException,status

from fastapi.security import HTTPBasic, HTTPBasicCredentials
app = FastAPI(title="fastapi authntication demo")


def verify_credentials(credentials:HTTPBasicCredentials):
    username="admin"
    password="admin@123"
    if credentials.username == username and credentials.password == password:
       # right Credentials
       return {
           "name": "yogi",
           "email": "test@tet.com",
           "mobile": "99999999",
         "address": "ttttttttttxz"
       }
    raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"}, 
    )
    
@app.get("/public")
def get_generl_info():
    return {
        "title": "FastApi Authentication Demo",
        "description": "learning to build apis"
    }
@app.post("/me")
def get_profile(username:str = Depends(verify_credentials)):
    return {
        "name": "yogi",
        "email": "test@test.com",
        "mobile": "999999999",
        "address": "xxxxxxxxxxxxxxx"
    }