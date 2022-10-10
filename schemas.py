from typing import List,Optional, Union
from pydantic import BaseModel

class ContactSchema (BaseModel):
    name : str
    country : str
    contactnum :int

    class Config():
        orm_mode = True

class UserSchema(BaseModel):
    name : str
    email : str
    password :str
   
    class Config():
        orm_mode = True  
        
class UserSchemaGet(BaseModel):
    id : int
    name : str
    email : str
    password :str
    creator : List=[]
   
    class Config():
        orm_mode = True
        
class ContactSchemaGet (BaseModel):
    id : int
    name : str
    country : str
    creation : UserSchema

    class Config():
        orm_mode = True


class login(BaseModel):
    username : str
    password : str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None