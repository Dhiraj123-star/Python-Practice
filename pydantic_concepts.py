from pydantic import BaseModel,validator
from typing import List

class User(BaseModel):
    username:str
    password:str
    email:str
    full_name:str
    phone_number:str

    @validator('email')
    def email_must_contain_at(cls,v):
        if '@' in v:
            raise ValueError("must contain'@' " )
        return v 
    @validator('phone_number')
    def phone_number_must_contain_dash(cls,v):
        if '-' not in v:
            raise ValueError('must contain "-"')
        return v

def create_user(user:User) -> dict :
    user_dict = user.dict()
    return user_dict

# validate teh data 

user_data = {
    'username':'john_doe',
    'password':'password@123',
    'email':'john_doeexample.com',
    'full_name':'joe doe',
    'phone_number':'8673731190'
}

user = User(**user_data) # show the validation error in email & phone_number 

created_user= create_user(user)

