from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Lista donde almacenaremos los usuarios (en este caso solo en memoria)
users = []

# Definir un modelo para el usuario
class User(BaseModel):
    name: str
    email: str

# API POST para crear un usuario
@app.post("/user/")
async def create_user(user: User):
    users.append(user)
    return {"message": "User created successfully", "user": user}

# API GET para obtener los usuarios
@app.get("/user/")
async def get_user():
    if not users:
        return {"message": "No users found"}
    return {"users": users}


from fastapi import FastAPI

app = FastAPI()

users = []

@app.post("/create-user/")
async def create_user(user: dict):
    users.append(user)
    return {"message": "User created successfully!"}

@app.get("/get-user/")
async def get_user():
    return {"users": users}
