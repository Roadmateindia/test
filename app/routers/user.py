from fastapi import APIRouter, Depends, HTTPException
from app.schemas.user import UserCreate, UserOut
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.crud import user as crud_user

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/users", response_model=UserOut)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return crud_user.create_user(db, user)

@router.get("/users", response_model=list[UserOut])
def list_users(db: Session = Depends(get_db)):
    return crud_user.get_users(db)

@router.get("/users/{user_id}", response_model=UserOut)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = crud_user.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/users/{user_id}", response_model=UserOut)
def update_user(user_id: int, user: UserCreate, db: Session = Depends(get_db)):
    return crud_user.update_user(db, user_id, user)

@router.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    crud_user.delete_user(db, user_id)
    return {"message": "User deleted"}
