from pydantic import BaseModel, validator
from typing import Optional
from datetime import date, datetime

class ExpenseBase(BaseModel):
    amount: float
    category: str
    description: Optional[str] = None
    date: str

   # @validator('date', pre=True)
    #def parse_date(cls, value):
       # if isinstance(value, str):
           # try:
               # return datetime.fromisoformat(value)
           # except ValueError:
               # return datetime.strptime(value, "%Y-%m-%dT%H:%M:%S")
       # return value

class ExpenseCreate(ExpenseBase):
    user_id: int

class Expense(ExpenseBase):
    id: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int

    class Config:
        orm_mode = True
