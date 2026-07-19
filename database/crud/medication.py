from sqlalchemy.orm import Session

from database.models import Medication


def create_medication(db: Session, **data) -> Medication:
    medication = Medication(**data)

    db.add(medication)
    db.commit()
    db.refresh(medication)

    return medication


def get_medication(db: Session, medication_id: int):
    return (
        db.query(Medication)
        .filter(Medication.id == medication_id)
        .first()
    )


def get_user_medications(db: Session, user_id: int):
    return (
        db.query(Medication)
        .filter(Medication.user_id == user_id)
        .all()
    )


def update_status(
    db: Session,
    medication_id: int,
    status: str,
):
    medication = get_medication(
        db,
        medication_id,
    )

    if medication is None:
        return None

    medication.status = status

    db.commit()
    db.refresh(medication)

    return medication


def delete_medication(
    db: Session,
    medication_id: int,
):
    medication = get_medication(
        db,
        medication_id,
    )

    if medication:
        db.delete(medication)
        db.commit()

    return medication