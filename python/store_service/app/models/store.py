from sqlalchemy import string, float, Integer,column
from app.db.base import Base

class Store(Base):
    __tablename__ = "stores"

    id = column(Integer, primary_key=True)
    name = column(string(50))
    address = column(string(100))
    city = column(string(50))
    area = column(string(200))
    address = column(string(200))