from sqlalchemy.orm import Session

from database.crud.medication import (
    create_medication,
    get_user_medications,
    update_status,
)


class MedicationService:

    @staticmethod
    def create(db: Session, data: dict):
        return create_medication(
            db,
            **data,
        )

    @staticmethod
    def get_all(
        db: Session,
        user_id: int,
    ):
        return get_user_medications(
            db,
            user_id,
        )

    @staticmethod
    def mark_taken(
        db: Session,
        medication_id: int,
    ):
        return update_status(
            db,
            medication_id,
            "Taken",
        )

    @staticmethod
    def mark_missed(
        db: Session,
        medication_id: int,
    ):
        return update_status(
            db,
            medication_id,
            "Missed",
        )