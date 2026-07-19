from pydantic import BaseModel, Field


class MedicationInput(BaseModel):
    medicine_name: str = Field(
        ...,
        min_length=2,
        max_length=100,
    )

    dosage: str = Field(
        ...,
        min_length=1,
    )

    frequency: str = Field(
        ...,
        min_length=1,
    )

    scheduled_time: str = Field(
        ...,
        description="24-hour HH:MM format",
    )

    notes: str = ""