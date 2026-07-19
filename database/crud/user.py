from sqlalchemy.orm import Session

from database.models import User


def create_user(db: Session, **user_data) -> User:
    user = User(**user_data)

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


def get_user_by_id(db: Session, user_id: int):
    return (
        db.query(User)
        .filter(User.id == user_id)
        .first()
    )


def get_all_users(db: Session):
    return db.query(User).all()


def delete_user(db: Session, user_id: int):
    user = get_user_by_id(db, user_id)

    if user:
        db.delete(user)
        db.commit()

    return user