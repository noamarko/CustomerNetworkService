from pydantic import BaseModel

class NameBoundary(BaseModel):
    first:str = None
    last:str = None
    
    # def __init__(self, first, last) -> None:
    #     self.first = first
    #     self.last = last

class FriendBoundary(BaseModel):
    email:str