from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas, database

app = FastAPI()

models.Base.metadata.create_all(bind=database.engine)

@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    return crud.create_user(db=db, user=user)

@app.post("/expenses/", response_model=schemas.Expense)
def create_expense(expense: schemas.ExpenseCreate, db: Session = Depends(database.get_db)):
    return crud.create_expense(db=db, expense=expense)

@app.get("/users/{user_id}/expenses/", response_model=list[schemas.Expense])
def read_expenses(user_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    return crud.get_expenses(db, user_id=user_id, skip=skip, limit=limit)
