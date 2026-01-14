from pydantic import BaseModel

class GoalCreate(BaseModel):
    title: str
    description: str | None = None

class GoalOut(BaseModel):
    id: int
    title: str
    description: str | None = None

    class Config:
        orm_mode = True

class GoalUpdate(BaseModel):
    title: str
    description: str | None = None
