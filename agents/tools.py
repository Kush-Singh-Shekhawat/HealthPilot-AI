from langchain_core.tools import tool


from langchain_core.tools import tool

from database.db import SessionLocal

from services.medication_service import MedicationService
from services.health_service import HealthService

from agents.extractors import (
    medication_extractor,
    health_extractor,
)

@tool
def add_medication(user_input: str) -> str:
    """
    Add a medication from natural language.
    """

    db = SessionLocal()

    try:
        medication = medication_extractor.invoke(user_input)

        MedicationService.create(
            db,
            {
                "user_id": 1,
                "medicine_name": medication.medicine_name,
                "dosage": medication.dosage,
                "frequency": medication.frequency,
                "scheduled_time": medication.scheduled_time,
                "status": "Scheduled",
                "notes": medication.notes,
            },
        )

        return (
            f"Medication '{medication.medicine_name}' "
            "added successfully."
        )

    finally:
        db.close()

@tool
def list_medications() -> str:
    """
    Show all medications.
    """

    db = SessionLocal()

    try:
        medications = MedicationService.get_all(
        db,
        user_id=1,
        )

        if not medications:
            return "No medications found."

        lines = []

        for med in medications:
            lines.append(
                f"- {med.medicine_name} "
                f"({med.dosage}) "
                f"at {med.scheduled_time}"
            )

        return "\n".join(lines)

    finally:
        db.close()

@tool
def log_health_metric(user_input: str) -> str:
    """
    Log health information.
    """

    db = SessionLocal()

    try:
        import re

        match = re.search(r"(\d+)\s*steps", user_input.lower())

        if match:
            metric = {
                "metric_type": "steps",
                "value": float(match.group(1)),
                "unit": "steps"
            }
        else:
            return "Couldn't identify the health metric."

        HealthService.create(
            db,
            {
                "user_id": 1,
                "metric_type": metric.metric_type,
                "value": metric.value,
                "unit": metric.unit,
            },
        )

        return (
            f"{metric.metric_type} "
            "recorded successfully."
        )

    finally:
        db.close()

