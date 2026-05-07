# making connection bredge between fastapi and postgresql

# u need to import this 3 from sqlalchemy 

#creat_engine  creates the connection to PostgreSQL

# sessionmaker creats a new session obj that helps to talk to  databse 

#declarative_base gives you a Base class that you inherit from — 

# it tells SQLAlchemy "hey this class is a database table, not a regular class."


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker , declarative_base
from dotenv import load_dotenv
import os 
load_dotenv()


# u need to put the url in a veriable all caps because that url is constant 
DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autoflush=False,bind=engine,autocommit = False)
# autocommit=False → don't save changes automatically, wait for us to say when
# autoflush=False → don't send changes to DB automatically
# bind=engine → use the engine we just created

Base = declarative_base()

def get_db():
    db = SessionLocal()

    try :
        yield db
    finally:
        db.close()    