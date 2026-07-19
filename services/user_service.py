from sqlalchemy.orm import Session

from database.crud.user import (
    create_user,
    get_all_users,
    get_user_by_id,
)


class UserService:

    @staticmethod
    def create(db: Session, user_data: dict):
        return create_user(
            db,
            **user_data
        )

    @staticmethod
    def get(db: Session, user_id: int):
        return get_user_by_id(
            db,
            user_id
        )

    @staticmethod
    def get_all(db: Session):
        return get_all_users(db)