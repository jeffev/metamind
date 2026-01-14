from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.goal import GoalCreate, GoalOut, GoalUpdate
from app.services.goal_service import create_goal, get_goals, update_goal, delete_goal
from app.db import get_db
from app.services.jwt_dependency import get_current_user

router = APIRouter(prefix="/goals", tags=["goals"])

@router.post("/", response_model=GoalCreate)
def create(data: GoalCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    return create_goal(db, user.id, data.title, data.description)

@router.get("/", response_model=list[GoalOut])
def list_all(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return get_goals(db, user.id)

@router.put("/{goal_id}", response_model=GoalOut)
def update(goal_id: int, data: GoalUpdate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    goal = update_goal(db, user.id, goal_id, data.title, data.description)
    if not goal:
        raise HTTPException(status_code=404, detail="Meta não encontrada")
    return goal

@router.delete("/{goal_id}")
def delete(goal_id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    ok = delete_goal(db, user.id, goal_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Meta não encontrada")
    return {"success": True}
