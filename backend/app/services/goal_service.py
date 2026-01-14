from sqlalchemy.orm import Session
from app.models import Goal

def create_goal(db: Session, user_id: int, title: str, description: str | None):
    goal = Goal(title=title, description=description, user_id=user_id)
    db.add(goal)
    db.commit()
    db.refresh(goal)
    return goal

def get_goals(db: Session, user_id: int):
    return db.query(Goal).filter(Goal.user_id == user_id).all()

def update_goal(db: Session, user_id: int, goal_id: int, title: str, description: str | None):
    goal = db.query(Goal).filter(Goal.id == goal_id, Goal.user_id == user_id).first()
    if not goal:
        return None
    goal.title = title
    goal.description = description
    db.commit()
    db.refresh(goal)
    return goal

def delete_goal(db: Session, user_id: int, goal_id: int):
    goal = db.query(Goal).filter(Goal.id == goal_id, Goal.user_id == user_id).first()
    if not goal:
        return False
    db.delete(goal)
    db.commit()
    return True
