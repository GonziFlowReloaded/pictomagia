from pydantic import BaseModel


class UserBase(BaseModel):
    email: str
    password: str
    password2: str
    birthdate: str


class UserCreate(UserBase):
    pass
