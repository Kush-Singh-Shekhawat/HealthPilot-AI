from config.llm import llm

from schemas.medication import MedicationInput
from schemas.health import HealthMetricInput


medication_extractor = llm.with_structured_output(
    MedicationInput
)

health_extractor = llm.with_structured_output(
    HealthMetricInput
)