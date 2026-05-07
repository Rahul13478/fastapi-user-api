from fastapi import APIRouter , HTTPException
from sqlalchemy.orm import Session
from schemas import UserRegister , UserLogin , New_data
from fastapi import Depends
from database import get_db
from sqlalchemy import select
from models import User
from auth import verify_password
from auth import verify_token
from auth import hash_password
from auth import create_token
from sqlalchemy import update

router  = APIRouter()

@router.get("/users")
def  get_users(db:Session = Depends(get_db),get_email : str = Depends(verify_token)):
    all_user = db.scalars(select(User)).all()
    return all_user


@router.post("/register")
def create_user(user:UserRegister,db:Session = Depends(get_db)):
     hashed = hash_password(user.password)
     new_user = User(name = user.name,email = user.email,password = hashed)
     db.add(new_user)
     db.commit()
     db.refresh(new_user)

     return new_user

@router.post("/login")
def user_login(login:UserLogin,db:Session = Depends(get_db)):
     found_user = db.query(User).filter_by(email=login.email).first()
     if found_user is None:
           raise HTTPException(status_code = 404, detail = "user not found ")
          
     check_pass = verify_password(plain_password=login.plain_password,hashed_password=found_user.password)
     if check_pass == True:
        pass_token = create_token(login.email)
        return pass_token
     if check_pass == False:
          raise HTTPException(status_code=401,detail="password incorrect")
     
@router.delete("/users/{user_id}")
def delete_user(user_id:int,db:Session = Depends(get_db),get_email : str = Depends(verify_token)):
     s = db.get(User,user_id)
     if s is  None :
         
           raise HTTPException(status_code = 404, detail = "user not found ")
        
     db.delete(s)
     db.commit()
     
     output_1 = {
         "message":"user deleted"
     }
     return output_1

@router.put("/users/{user_id}")
def update_data(data:New_data,user_id:int,db:Session = Depends(get_db),get_email : str = Depends(verify_token)):
     s = db.get(User,user_id)
     if s is  None :
         
           raise HTTPException(status_code = 404, detail = "user not found ")
   
     stmt = (
          update(User)
          .where(User.id==user_id)
          .values({"name":data.name,
                   "email":data.email})
     )
     db.execute(stmt)
     db.commit()
     return{"message":"user updated "}
     
          
