from datetime import datetime

from src.exceptions import WrongDateFormat


def format_date_response(date_input: datetime | None) -> str | None:
    return date_input.strftime("%Y-%m-%d %H:%M:%S") if date_input else None


def validate_date(date_string: str) -> str:
    try:
        datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S')
    except ValueError:
        raise WrongDateFormat(details='Invalid date format. Should be YYYY-MM-DD HH:MM:SS')
    return date_string