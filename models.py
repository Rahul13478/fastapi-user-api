# models.py — defines database tables as Python classes
# each class = one table in PostgreSQL
# each variable inside the class = one column in that table
# Base connects these classes to the actual database


from database import Base
from sqlalchemy import  Column , Integer, String

class User(Base):
    __tablename__  = "users"
    id = Column(Integer , primary_key=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

