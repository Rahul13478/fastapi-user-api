from pydantic import BaseModel

class UserRegister(BaseModel):
     name : str
     email : str
     password : str

class UserLogin(BaseModel):
     email : str
     plain_password : str     

class New_data(BaseModel):
    name : str
    email : str     