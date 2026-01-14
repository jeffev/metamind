from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import get_db
from app.schemas.user import UserCreate, UserOut
from app.services.user_service import get_by_email, create_user
from app.schemas.auth import LoginIn, TokenOut
from app.services.auth_service import create_access_token
from app.services.user_service import get_by_email, verify_password
from fastapi.security import OAuth2PasswordRequestForm


router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register", response_model=UserOut)
def register(user: UserCreate, db: Session = Depends(get_db)):
    if get_by_email(db, user.email):
        raise HTTPException(status_code=400, detail="Email já cadastrado")
    return create_user(db, user.email, user.password)

@router.post("/login", response_model=TokenOut)
def login(form: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = get_by_email(db, form.username)  # aqui é o email
    if not user or not verify_password(form.password, user.password):
        raise HTTPException(status_code=401, detail="Credenciais inválidas")

    token = create_access_token({"sub": str(user.id)})
    return {"access_token": token, "token_type": "bearer"}