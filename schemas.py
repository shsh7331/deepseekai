from pydantic import BaseModel
from datetime import date
class UserCreate(BaseModel):
    username: str
    email: str
    password: str
class CategoryOut(BaseModel):
    id: int
    category_name: str
    class Config:
        orm_mode = True
class ExpenseCreate(BaseModel):
    user_id: int
    expense_name: str
    expense_amount: float
    expense_category: int
    expense_date: date
class ExpenseOut(BaseModel):
    id: int
    expense_name: str
    expense_amount: float
    expense_date: date
    class Config:
        orm_mode = True
