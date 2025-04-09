from sqlalchemy import Column, Integer, String, Date, ForeignKey, Numeric, TIMESTAMP, CheckConstraint
from sqlalchemy.orm import relationship
from database import Base
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    created_at = Column(TIMESTAMP, server_default="now()")
    expenses = relationship("Expense", back_populates="user")
class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True, index=True)
    category_name = Column(String(50), unique=True, nullable=False)
class Expense(Base):
    __tablename__ = 'expenses'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    expense_name = Column(String(100), nullable=False)
    expense_amount = Column(Numeric(10, 2), nullable=False)
    expense_category = Column(Integer, ForeignKey("categories.id"), nullable=False)
    expense_date = Column(Date, nullable=False)
    user = relationship("User", back_populates="expenses")
