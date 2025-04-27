from pydantic import BaseModel, EmailStr


class UserSignUpSchema(BaseModel):
    name: str
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class ChangePassword(BaseModel):
    new_password:str
    email:EmailStr
    code:str

