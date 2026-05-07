# FastAPI User API

## What is this?
A REST API built with FastAPI that allows users to register, 
login, and manage their data. Includes JWT authentication 
and PostgreSQL database.

## Technologies used
- Python
- FastAPI
- PostgreSQL
- SQLAlchemy (ORM)
- JWT (Authentication)
- bcrypt (Password hashing)

## How to run
1. Install dependencies:
pip install -r requirements.txt

2. Create a .env file with:
DATABASE_URL=your_database_url
SECRET_KEY=your_secret_key

3. Run the server:
uvicorn main:app --reload

4. Open docs at:
http://127.0.0.1:8000/docs