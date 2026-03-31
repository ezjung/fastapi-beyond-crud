from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}

# Path parameter
@app.get('/greet/{username}')
async def greet(username:str):
   return {"message":f"Hello {username}"}

# Query parameter

user_list = [
   "Jerry",
   "Joey",
   "Phil",
   "Sungsoon"
]

@app.get('/search')
async def search_for_user(q :str):
    for user in user_list:
        if q.lower() == user.lower():
            return {"message":f"User {q} found"}
    return {"message":f"User {q} not found"}

# Optional query parameter
from typing import Optional

@app.get('/greet_optional')
async def greet_optional(q :Optional[str] = None):
    if q:
        return {"message":f"Hello {q}"}
    return {"message":f"Hello world"}

# Request body
from pydantic import BaseModel

class User(BaseModel):
    username: str
    email: str

@app.post('/create_user')
async def create_user(user: User):
    new_user = {
        "username": user.username,
        "email": user.email
    }
    user_list.append(new_user)
    return {"message":f"User {new_user['username']} created"}

# Request Headers
from fastapi import Header

@app.get('/get_headers')
async def get_all_request_headers(
    user_agent: Optional[str] = Header(None),
    accept_encoding: Optional[str] = Header(None),
    referer: Optional[str] = Header(None),
    connection: Optional[str] = Header(None),
    accept_language: Optional[str] = Header(None),
    host: Optional[str] = Header(None),
):
    request_headers = {}
    request_headers["User-Agent"] = user_agent
    request_headers["Accept-Encoding"] = accept_encoding
    request_headers["Referer"] = referer
    request_headers["Accept-Language"] = accept_language
    request_headers["Connection"] = connection
    request_headers["Host"] = host

    return request_headers


