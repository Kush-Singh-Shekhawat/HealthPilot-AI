def validate_positive_number(value, field_name):
    if value < 0:
        raise ValueError(f"{field_name} cannot be negative.")


def validate_age(age):
    if age < 0 or age > 120:
        raise ValueError("Invalid age.")


def validate_water_intake(litres):
    if litres < 0 or litres > 20:
        raise ValueError("Invalid water intake.")