from fastapi import FastAPI
from app.database import engine, Base
from app.routers import user, project, client, message

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(user.router, prefix="/user", tags=["Users"])
app.include_router(project.router, prefix="/project", tags=["Projects"])
app.include_router(client.router, prefix="/client", tags=["Clients"])
app.include_router(message.router, prefix="/message", tags=["Messages"])

@app.get("/")
def root():
    return {"message": "✅ FastAPI backend is running!"}