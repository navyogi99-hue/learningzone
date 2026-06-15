from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials

app = FastAPI(title="fastapi authentication demo")

security = HTTPBasic()


def verify_credentials(credentials: HTTPBasicCredentials = Depends(security)):
    username = "admin"
    password = "admin@123"
    if credentials.username == username and credentials.password == password:
        return {
            "name": "yogi",
            "email": "test@test.com",
            "mobile": "999999999",
            "address": "xxxxxxxxxxxxxxx",
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
    return username