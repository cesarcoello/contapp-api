import json
import uvicorn
from typing import Union
from fastapi import FastAPI, HTTPException, Request
from utils.database import fetch_query_as_json
from fastapi.middleware.cors import CORSMiddleware

from models.UserLogin import UserLogin
from models.UserRegister import UserRegister

from controllers.google import login_google , auth_callback_google
from controllers.firebase import register_user_firebase, login_user_firebase

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True
)

@app.get("/")
async def read_root():
    query = "select * from contapp.personas"
    try:
        result = await fetch_query_as_json(query)
        result_dict = json.loads(result)
        return { "data": result_dict, "version": "0.0.3" }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)

@app.get("/login/google")
async def logingoogle():
    return await login_google()

@app.get("/auth/google/callback")
async def authcallbackgoogle(request: Request):
    return await auth_callback_google(request)

@app.post("/register")
async def register(user: UserRegister):
    return await register_user_firebase(user)

@app.post("/login/custom")
async def login_custom(user: UserRegister):
    return await login_user_firebase(user)