from fastapi import FastAPI
from app.db import engine, Base
from app.routes.auth import router as auth_router
from app.routes.goals import router as goals_router

app = FastAPI(title="MetaMind API")
Base.metadata.create_all(bind=engine)

app.include_router(auth_router)
app.include_router(goals_router)

@app.get("/")
def health():
    return {"status": "ok"}
