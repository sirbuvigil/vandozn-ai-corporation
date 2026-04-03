import re


def is_valid_email(email: str) -> bool:
    pattern = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"
    return re.match(pattern, email) is not None


def is_non_empty_string(value: str) -> bool:
    return isinstance(value, str) and value.strip() != ""


def is_positive_int(value) -> bool:
    try:
        return int(value) > 0
    except Exception:
        return False
