import re


def is_phone(field):
    result = re.fullmatch(r'[+7]\d{10}', field)
    return result


def is_email(field):
    result = re.fullmatch(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)', field)
    return result


def is_date(field):
    pattern = r'((\d{4})\-(\d{2})\-(\d{2}))|(\d{2}\.(\d{2})\.(\d{4}))'
    result = re.fullmatch(pattern, field)
    return result


def check(field):
    if is_date(field):
        return "date"
    elif is_phone(field):
        return "phone"
    elif is_email(field):
        return "email"
    else:
        return "text"
