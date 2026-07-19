from pydantic import BaseModel
from datetime import date


class HealthMetricInput(BaseModel):
    record_date: date

    steps: int = 0

    water: float = 0

    sleep: float = 0

    calories: int = 0

    weight: float

    heart_rate: int = 0