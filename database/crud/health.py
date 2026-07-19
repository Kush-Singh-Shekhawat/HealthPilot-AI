from sqlalchemy.orm import Session

from database.models import HealthMetric


def add_metric(
    db: Session,
    **data,
):
    metric = HealthMetric(**data)

    db.add(metric)
    db.commit()
    db.refresh(metric)

    return metric


def get_history(
    db: Session,
    user_id: int,
):
    return (
        db.query(HealthMetric)
        .filter(
            HealthMetric.user_id == user_id
        )
        .all()
    )