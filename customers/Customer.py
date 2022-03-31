from tokenize import Name
from pydantic import BaseModel
from customers.NameBoundary import NameBoundary

class Customer(BaseModel):
    name:NameBoundary
    email:str
    password:str
    birthdate:str


class CustomerBoundary(BaseModel):
    name:NameBoundary = None
    email:str = None
    birthdate:str = None

    def make_cus_bound_from_cus(self, cus:Customer):
        self.name = cus.name
        self.email = cus.email
        self.birthdate = cus.birthdate
        return self

class CustomerUpdater(BaseModel):
    name:NameBoundary = None
    password:str = None
    birthdate:str = None