from typing import List
from pydantic import BaseModel


class UserBase(BaseModel):
    firstname: str
    lastname: str
    email: str


class UserIn(UserBase):
    password: str

    class Config:
        schema_extra = {
            "example": {
                "firstname": "john",
                "lastname": "doe",
                "email": "john.doe@example.com",
                "password": "aze123!",
            }
        }


class UserOut(UserBase):
    id: str


class UserList(BaseModel):
    data: List[UserOut]
    total: int
    page: int
    per_page: int


class Login(BaseModel):
    email: str
    password: str

    class Config:
        schema_extra = {
            "example": {"email": "john.doe@example.com", "password": "aze123!"}
        }


class Token(BaseModel):
    access_token: str
    expires: float
    email: int
    tuid: str
