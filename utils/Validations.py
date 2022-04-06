import datetime
import re
from customers.Customer import NameBoundary
from fastapi import HTTPException


def validateEmail(email):
    if not email:
        raise HTTPException(status_code=400, detail="Email is required")
    # regular expression for validating an Email
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    if re.fullmatch(regex, email):
        return True
    else:
        raise HTTPException(status_code=400, detail="Email is not valid")


def validateName(name: NameBoundary):
    if not name:
        raise HTTPException(status_code=400, detail="Name is required: first and last ")
    if not name.first or not name.first.strip():
        raise HTTPException(status_code=400, detail="First name can not be empty")
    elif not name.last or not name.last.strip():
        raise HTTPException(status_code=400, detail="Last name can not be empty")
    else:
        return True

def validateFirstOrLast(firstOrLast:str, type:str):
    if not firstOrLast and not firstOrLast.strip():
        raise HTTPException(status_code=400, detail=f"{type} name can not be empty")

def validatePassword(password: str):
    if not password:
        raise HTTPException(
        status_code=400, detail="Password is required")
    if len(password) < 5:
        raise HTTPException(
            status_code=400, detail="Password must contain at least 5 letters")
    elif not bool(re.search(r'\d', password)):
        raise HTTPException(
            status_code=400, detail="Password must contain at least one digit")
    else:
        return True


def validateBirthDate(birth_date: str):
    if not birth_date:
        raise HTTPException(
        status_code=400, detail="Birth Date is required")
    try:
        x = datetime.datetime.strptime(birth_date, '%d-%m-%Y')
        assert x < datetime.datetime.today()
        return True
    except ValueError:
        raise HTTPException(
            status_code=400, detail="Incorrect date format, should be DD-MM-YYYY")
    except AssertionError:
        raise HTTPException(status_code=400, detail="Incorrect birth-date")


def validateRoles(roles: list):
    if roles is None:
        raise HTTPException(status_code=400, detail="roles is required")
    for role in roles:
        if not role:
            raise HTTPException(status_code=400, detail="Role can not be empty")
        return True
