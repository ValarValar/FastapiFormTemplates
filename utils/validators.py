import datetime

import phonenumbers
from phonenumbers import carrier
from pydantic import EmailStr



def phone_validator(phone_number: str):
    phonenumbers.parse(phone_number, None)


def is_phone_number(phone_number: str) -> bool:
    try:
        phone_validator(phone_number)
        return True
    except Exception as e:
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


def convert_value_to_type(input_value:str) -> str:
    if is_date(input_value):
        return 'date'
    elif is_phone_number(input_value):
        return 'phone'
    elif is_email(input_value):
        return 'email'
    else:
        return 'text'

a = ['hi@mail.ru', 'hi@', '12.15.2022', '15.12.2022', '+7 989 702 62 68', '99897026268', '79875397026268']
for x in a:
    print(f'{x} its type is {convert_value_to_type(x)}')
ro_number = phonenumbers.parse("+79897026268", "RU")
carrier.name_for_number(ro_number, "ru")
