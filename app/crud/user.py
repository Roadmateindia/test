from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate

def create_user(db: Session, user: UserCreate) -> User:
    """
    Create a new user in the database.
    """
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_users(db: Session) -> list[User]:
    """
    Retrieve all users from the database.
    """
    return db.query(User).all()

def get_user(db: Session, user_id: int) -> User | None:
    """
    Retrieve a user by ID.
    """
    return db.query(User).filter(User.id == user_id).first()

def update_user(db: Session, user_id: int, user_data: UserCreate) -> User | None:
    """
    Update an existing user.
    """
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        for key, value in user_data.dict().items():
            setattr(user, key, value)
        db.commit()
        db.refresh(user)
    return user

def delete_user(db: Session, user_id: int) -> User | None:
    """
    Delete a user by ID.
    """
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
    return user