from distutils.sysconfig import customize_compiler
from urllib import response
from customers.NameBoundary import NameBoundary
from fastapi import FastAPI, HTTPException
from typing import Optional


# from pydantic import BaseModel
from customers.Customer import Customer, CustomerBoundary


app = FastAPI()
customers = []

@app.get("/customers/byEmail/{email}")
async def retriveCustomerDetails(email:str):
    # return email
    for c in customers:
        if c.email == email:
            # return CustomerBoundary(name=c.name, email=c.email)
            return {key:vars(c)[key] for key in vars(c) if not key == "password"}

    raise HTTPException(status_code=404, detail="Customer not found") 


@app.get("/customers/login/{email}")
async def login(email:str, password:str):
    for c in customers:
        if c.email == email:
            if c.password == password:
                return {key:vars(c)[key] for key in vars(c) if not key == "password"}
            else:
                raise HTTPException(status_code=401, detail="Incorrect password") 

    raise HTTPException(status_code=404, detail="Customer not found") 


@app.put("/customers/{email}", response_model = CustomerBoundary)
async def updateCostumer(email:str, customer:CustomerBoundary):
    for c in customers:
        if c.email == email:
            if customer.name:
                c.name = customer.name
            if customer.password:
                c.password = customer.password
            return {key:vars(c)[key] for key in vars(c) if not key == "password"}
    
    raise HTTPException(status_code=404, detail="Customer not found") 


@app.post("/customers")
async def createCustomer(firstName:str, lastName:str, email:str, password:str):
    name = NameBoundary(first= firstName, last=lastName)
    customer= Customer(name, email, password)
    if customer.email in [c.email for c in customers]: 
        raise HTTPException(status_code=500, detail="Customer already exist")

    customers.append(customer)
    return customer

    
