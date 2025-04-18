from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager
DATABASE_URL = "postgresql://deepfinance_db_user:hWdcB41ynmNIfXELENWVhQJPolBpkdEb@dpg-cvqsje3e5dus73fu0lv0-a/deepfinance_db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()
@contextmanager
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


