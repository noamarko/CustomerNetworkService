from tokenize import Name
from pydantic import BaseModel
from customers.NameBoundary import NameBoundary

class Customer():

    def __init__(self, name:NameBoundary, email, password) -> None:
        self.name = name
        self.email = email
        self.password = password

class CustomerBoundary(BaseModel):
    name:NameBoundary = None
    email:str = None
    # def __init__(self, name = None, email = None , password=None) -> None:
    #     self.name = name
    #     self.email = email
    #     self.password = password

