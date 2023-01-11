import datetime

from pydantic import EmailStr


def phone_validator(phone_number: str):
    if phone_number[0] == ' ':
        phone_number = phone_number.replace(' ', '+', 1)
    phone_number = ''.join(phone_number.split())
    PHONE_NUMBER_LEN = 12
    # '7' should be after plus sign
    if phone_number[1] == '7':
        if phone_number[1:].isdigit() and len(phone_number) == PHONE_NUMBER_LEN:
            return
    raise ValueError


def is_phone_number(phone_number: str) -> bool:
    try:
        phone_validator(phone_number)
        return True
    except ValueError:
        return False


def date_validator(date: str):
    try:
        datetime.datetime.strptime(date, '%d.%m.%Y')
    except ValueError:
        datetime.datetime.strptime(date, '%Y-%m-%d')


def is_date(date: str) -> bool:
    try:
        date_validator(date)
        return True
    except ValueError:
        return False


def email_validator(email: str):
    EmailStr.validate(email)


def is_email(email: str):
    try:
        email_validator(email)
        return True
    except ValueError:
        return False


def convert_value_to_type(input_value: str) -> str:
    if is_date(input_value):
        return 'date'
    elif is_phone_number(input_value):
        return 'phone'
    elif is_email(input_value):
        return 'email'
    else:
        return 'text'


def convert_dict_values_to_type(input: dict) -> dict:
    for key in input:
        input[key] = convert_value_to_type(input[key])
    return input
