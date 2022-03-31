import fastapi_pagination
import datetime

from distutils.sysconfig import customize_compiler
from urllib import response
from fastapi import FastAPI, HTTPException
from typing import Optional
from fastapi_pagination import Page, add_pagination, paginate


# from pydantic import BaseModel
from customers.Customer import Customer, CustomerBoundary, CustomerUpdater
from customers.NameBoundary import NameBoundary, FriendBoundary

SORT_OPTIONS = {'date':lambda x:datetime.datetime.strptime(x.birthdate, "%d-%m-%Y").timestamp(),
                'email':lambda x:x.email,'name':lambda x:x.name.first+x.name.last} 
app = FastAPI()
customers = {
  "nadav@gmail.com": Customer(name=NameBoundary(first='nadav',last='s'), email='nadav@gmail.com', password='123',birthdate='04-09-1993',roles=["goldCustomer","platinumClub","primeService"]),
  "lidor@hotmail.com": Customer(name=NameBoundary(first='lidor',last='amitay'), email='lidor@hotmail.com', password='123',birthdate='04-01-1992',roles=["goldCustomer","platinumClub","   "]),
  "noam@gmail.com": Customer(name=NameBoundary(first='noam',last='marko'), email='noam@gmail.com', password='123',birthdate='01-08-1994',roles=["lowService"]),
  "nissan@walla.co.il": Customer(name=NameBoundary(first='nissan',last='dalva'), email='nissan@walla.co.il', password='123',birthdate='04-10-1993',roles=["freeAcount"]),
}

friends = {}


@app.get("/customers/byEmail/{email}")
async def retriveCustomerDetails(email:str):
    if email in customers.keys():
        c = customers[email]
        return CustomerBoundary().make_cus_bound_from_cus(c)
    
    raise HTTPException(status_code=404, detail="Customer not found") 


@app.get("/customers/login/{email}")
async def login(email:str, password:str):
    
    if email in customers.keys():
        c = customers[email]
        if c.password == password:
            return CustomerBoundary().make_cus_bound_from_cus(c)
        else:
            raise HTTPException(status_code=401, detail="Incorrect password") 

    raise HTTPException(status_code=404, detail="Customer not found") 

#TODO: validations
@app.post("/customers")
async def createCustomer(fullname:NameBoundary, email:str, password:str,birthdate:str,roles:list):
    global customers
    if email in customers.keys(): 
        raise HTTPException(status_code=500, detail="Customer already exist")
    customers[email] = Customer(name=fullname, email=email, password=password,birthdate=birthdate,rolse=roles) 
    return CustomerBoundary().make_cus_bound_from_cus(customers[email])

#TODO: validations 
@app.put("/customers/{email}", response_model = CustomerBoundary)
async def updateCostumer(email:str, customer:CustomerUpdater):
    global customers
    if email in customers.keys():
        c = customers[email]
        if customer.name:
            c.name = customer.name
        if customer.password:
            c.password = customer.password
        return CustomerBoundary().make_cus_bound_from_cus(c)
    
    raise HTTPException(status_code=404, detail="Customer not found") 


@app.put('/customers/{email}/friends')
async def friends_connection(email:str, friend:FriendBoundary):
    global friends
    if email in customers.keys() and friend.email in customers.keys():
        
        if friend.email not in friends.keys():
            friends[friend.email] = []
        if email not in friends.keys():
            friends[email] = []
        if friend.email not in friends[email]:
            friends[email].append(friend.email)
            friends[friend.email].append(email)
    else:
        raise HTTPException(status_code=404, detail="Customer not found") 


@app.get('/customers/{email}/friends',response_model=Page[CustomerBoundary])
async def customer_friends_list(email:str):
    if email in friends.keys():
        return paginate([CustomerBoundary().make_cus_bound_from_cus(c) for c in [customers[email] for email in friends[email]]])
    raise HTTPException(status_code=404, detail="Customer not found")   

        
@app.delete('/customers')
async def delete_all_customers():
    customers.clear()
    return customers


@app.get('/customers/search',response_model=Page[CustomerBoundary])
async def search_customer(sortBy=None, sortOrder=None, criteriaType=None,criteriaValue =None):
    cus_boundary_list = [CustomerBoundary().make_cus_bound_from_cus(c) for c in [customers[email] for email in customers.keys()]]
    if criteriaType=='byBirthYear' and criteriaValue:
        cus_boundary_list = [CustomerBoundary().make_cus_bound_from_cus(c) for c in [customers[email] for email in customers.keys()] if c.birthdate.split('-')[-1] == criteriaValue]
    elif criteriaType=='byEmailDomain' and criteriaValue:
        cus_boundary_list = [CustomerBoundary().make_cus_bound_from_cus(c) for c in [customers[email] for email in customers.keys()] if c.email.split("@")[-1] == criteriaValue]
    elif criteriaType=='byRole' and criteriaValue:
        cus_boundary_list = [CustomerBoundary().make_cus_bound_from_cus(c) for c in [customers[email] for email in customers.keys()] if criteriaValue in c.roles]
    if sortBy:
        if sortBy in SORT_OPTIONS:
            return paginate(sorted(cus_boundary_list,key=SORT_OPTIONS[sortBy], reverse=True if sortOrder=='DESC' else False))
        else:
            HTTPException(status_code=400, detail="Invalid sort parameter") 
    return paginate(sorted(cus_boundary_list,key=SORT_OPTIONS['email']))    


@app.get('/friends/')
async def customer_friends_list():
    return friends


@app.get('/customers/{email}/friends/secondLevel',response_model=Page[CustomerBoundary])
async def second_level_customer_friends_list(email:str):
    if email in friends:
        third = first = friends[email]
        second = []
        for e2 in first:
            second.extend(friends[e2])
        third.extend(second)
        return paginate([CustomerBoundary().make_cus_bound_from_cus(c) for c in [customers[email] for email in set(third)]])

add_pagination(app)