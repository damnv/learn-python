from fastapi import FastAPI
from routes import user, student

app = FastAPI()

# app.include_router(user.router)
app.include_router(student.router)



