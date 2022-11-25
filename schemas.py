from pydantic import BaseModel, Field, EmailStr
from datetime import datetime,date,time


class User(BaseModel):
    first_name:str
    last_name:str
    password:str
    email:str
    is_admin:bool
    date_created:datetime

class Countries(BaseModel):
    name:str
    abbreviation:str
    class Config:
        orm_mode=True
class Holidays(BaseModel):
    country:str
    holiday:datetime
    class Config:
        orm_mode=True


class ResetPass(BaseModel):
    pin:str
    user_id:int
    is_used:bool
    expiry_date:datetime
    date_created:datetime

class PasswordResetRequest(BaseModel):
    email: EmailStr = Field(...)

class PasswordReset(BaseModel):
    password: str = Field(...)
    confirm_password: str = Field(...)


class UserBase(BaseModel):
    first_name: str
    last_name:str
    email: EmailStr

class UserCreate(UserBase):
    password:str=Field(min_length=8, description='password minimum length is 8 characters')
    class Config:
        orm_mode = True


class Login(BaseModel):
    email:EmailStr
    password:str
class UserDetails(UserBase):
    id: str
    first_name:str
    last_name:str
    is_admin:bool
    date_created:datetime

    class Config:
        orm_mode=True
from dotenv import load_dotenv
import os
load_dotenv()
#from fastapi_jwt_auth import AuthJWT
SECRET_KEY='random'

class Settings(BaseModel):
    authjwt_secret_key: str = SECRET_KEY
    authjwt_token_location:set ={'cookies','headers'}
    authjwt_access_cookie_key:str='access_token'
    authjwt_refresh_cookie_key:str='refresh_token'
    authjwt_cookie_csrf_protect: bool = False
    authjwt_cookie_samesite:str ='lax'


# @AuthJWT.load_config
def get_config():
    return Settings()


class PydanticReview(BaseModel):
    review:str
    id: int
    # first_name: str

    class Config:
        orm_mode = True

