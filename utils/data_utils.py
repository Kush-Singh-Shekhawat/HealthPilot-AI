from datetime import datetime


def current_timestamp():
    return datetime.now()


def current_date():
    return datetime.now().date()