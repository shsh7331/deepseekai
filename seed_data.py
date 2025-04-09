from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Base, User, Category, Expense
from datetime import date
# Create tables if they don't exist
Base.metadata.create_all(bind=engine)
# Sample data
users = [
    {"username": "alice", "email": "alice@example.com", "password": "alice123"},
    {"username": "bob", "email": "bob@example.com", "password": "bob123"},
    {"username": "carol", "email": "carol@example.com", "password": "carol123"},
]
categories = ["Food", "Transport", "Rent", "Entertainment", "Utilities", "Healthcare", "Other"]
expenses = [
    # Alice (id=1)
    {"user_id": 1, "expense_name": "Groceries at Walmart", "expense_amount": 85.50, "expense_category": 1, "expense_date": date(2025, 3, 15)},
    {"user_id": 1, "expense_name": "Uber to office", "expense_amount": 13.25, "expense_category": 2, "expense_date": date(2025, 3, 16)},
    {"user_id": 1, "expense_name": "Monthly Rent", "expense_amount": 950.00, "expense_category": 3, "expense_date": date(2025, 3, 1)},
    
    # Bob (id=2)
    {"user_id": 2, "expense_name": "Dinner with friends", "expense_amount": 42.00, "expense_category": 1, "expense_date": date(2025, 3, 10)},
    {"user_id": 2, "expense_name": "Netflix Subscription", "expense_amount": 15.99, "expense_category": 4, "expense_date": date(2025, 3, 5)},
    {"user_id": 2, "expense_name": "Bus Pass", "expense_amount": 50.00, "expense_category": 2, "expense_date": date(2025, 3, 6)},
    
    # Carol (id=3)
    {"user_id": 3, "expense_name": "Doctor Appointment", "expense_amount": 120.00, "expense_category": 6, "expense_date": date(2025, 3, 8)},
    {"user_id": 3, "expense_name": "Electricity Bill", "expense_amount": 60.75, "expense_category": 5, "expense_date": date(2025, 3, 4)},
    {"user_id": 3, "expense_name": "Groceries", "expense_amount": 72.40, "expense_category": 1, "expense_date": date(2025, 3, 9)},
]
def seed():
    db: Session = SessionLocal()
    try:
        # Add users
        if db.query(User).count() == 0:
            for user in users:
                db.add(User(**user))
        
        # Add categories
        if db.query(Category).count() == 0:
            for cat in categories:
                db.add(Category(category_name=cat))
        db.commit()
        # Add expenses (after committing users + categories to get proper IDs)
        if db.query(Expense).count() == 0:
            for exp in expenses:
                db.add(Expense(**exp))
            db.commit()
        print("Database seeded successfully.")
    finally:
        db.close()
if __name__ == "__main__":
    seed()
