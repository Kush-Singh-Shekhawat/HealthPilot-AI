from sqlalchemy.orm import Session

from database.crud.health import (
    add_metric,
    get_history,
)


class HealthService:

    @staticmethod
    def add(
        db: Session,
        data: dict,
    ):
        return add_metric(
            db,
            **data,
        )

    @staticmethod
    def history(
        db: Session,
        user_id: int,
    ):
        return get_history(
            db,
            user_id,
        )