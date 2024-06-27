from fastapi import FastAPI
from typing import List
import crud, schemas

app = FastAPI()

@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate):
    return crud.create_user(user)

@app.post("/expenses/", response_model=schemas.Expense)
def create_expense(expense: schemas.ExpenseCreate):
    print(expense)
    return crud.create_expense(expense)

#@app.get("/users/{user_id}/expenses/", response_model=List[schemas.Expense])
@app.get("/users/{user_id}/expenses/")
def read_expenses(user_id: int, skip: int = 0, limit: int = 100):
    return crud.get_expenses(user_id, skip, limit)
