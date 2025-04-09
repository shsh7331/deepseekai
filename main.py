from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Base, User, Category, Expense
from database import engine, SessionLocal
import schemas
app = FastAPI()
Base.metadata.create_all(bind=engine)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
@app.post("/users/")
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
@app.get("/categories/", response_model=list[schemas.CategoryOut])
def get_categories(db: Session = Depends(get_db)):
    return db.query(Category).all()
@app.post("/expenses/")
def create_expense(exp: schemas.ExpenseCreate, db: Session = Depends(get_db)):
    db_exp = Expense(**exp.dict())
    db.add(db_exp)
    db.commit()
    db.refresh(db_exp)
    return db_exp
@app.get("/expenses/{user_id}", response_model=list[schemas.ExpenseOut])
def get_user_expenses(user_id: int, db: Session = Depends(get_db)):
    return db.query(Expense).filter(Expense.user_id == user_id).all()
