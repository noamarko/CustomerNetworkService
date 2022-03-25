from mimetypes import init
from pydantic import BaseModel

class Customer(BaseModel):
    name:str
    email:str
    password:str

    def __init__(self, name, email, password) -> None:
        self.name = name
        self.email = email
        self.password = password

class DefaultCustomer(BaseModel):
    name:str = None
    email:str = None
    password:str = None
    def __init__(self, name = None, email = None , password=None) -> None:
        self.name = name
        self.email = email
        self.password = password