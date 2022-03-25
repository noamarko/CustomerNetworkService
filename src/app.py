from distutils.sysconfig import customize_compiler
from urllib import response
from fastapi import FastAPI, HTTPException
from typing import Optional


# from pydantic import BaseModel
from customers.Customer import Customer, DefaultCustomer


app = FastAPI()
customers = []

@app.get("/customers/byEmail/{email}")
async def retriveCustomerDetails(email:str):
    for c in customers:
        if c.email == email:
            return {key:vars(c)[key] for key in vars(c) if not key == "password"}

    raise HTTPException(status_code=404, detail="Customer not found") 


@app.get("/customers/login/{email}")
async def login(email:str, password:str):
    # return {"email":email, "password":password}
    for c in customers:
        if c.email == email:
            if c.password == password:
                return {key:vars(c)[key] for key in vars(c) if not key == "password"}
            else:
                raise HTTPException(status_code=403, detail="Incorrect password") 

    raise HTTPException(status_code=404, detail="Customer not found") 


@app.put("/customers/{email}", response_model = DefaultCustomer)
async def updateCostumer(email:str, customer:DefaultCustomer):
    pass
    # for c in customers:
    #     if c.email == email:
    #         if name:
    #             c.name = name
    #         if password:
    #             c.password = password
    #         return {key:vars(c)[key] for key in vars(c) if not key == "password"}

    # raise HTTPException(status_code=404, detail="Customer not found") 


@app.post("/customers")
async def createCustomer(name:str, email:str, password:str):
    customer= Customer(name, email, password)
    if customer.email in [c.email for c in customers]: 
        raise HTTPException(status_code=500, detail="Customer already exist")

    customers.append(customer)
    return customer

    
