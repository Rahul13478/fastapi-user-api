# passlib    → a library that manages password hashing
#              (it is the wrapper that makes bcrypt easy to use)

# bcrypt     → the actual hashing algorithm
#              (passlib uses bcrypt under the hood)

# python-jose → handles JWT tokens
#               (jose stands for JavaScript Object Signing and Encryption)
#               (creates and verifies tokens)


# passlib  = the chef
# bcrypt   = the recipe the chef uses
# jose     = the ticket machine (makes and checks tokens)


from passlib.context import CryptContext
from jose import jwt , JWTError
from datetime import datetime , timedelta
from fastapi.security import  HTTPBearer ,HTTPAuthorizationCredentials
from fastapi import Depends , status , HTTPException
from dotenv import load_dotenv
import os 
load_dotenv()


pwd_context = CryptContext(schemes=["bcrypt"])
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
oauth2_sheme = HTTPBearer()
def hash_password(password:str):
    return pwd_context.hash(password)

def verify_password(plain_password,hashed_password):
    return pwd_context.verify(plain_password,hashed_password)


def create_token( Email:str ):
    now  = datetime.now()
    expire_time = now + timedelta( minutes= 30 )
    payload = {
        "sub":Email,
        "exp":expire_time
    }
    token = jwt.encode(payload,SECRET_KEY,algorithm=ALGORITHM)
    return token



def verify_token(token: HTTPAuthorizationCredentials =Depends(oauth2_sheme)):
    credential_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="could not valid credential",
        headers={"www-Authenticate":"Bearer"}
    )
    try :
     payload = jwt.decode(token.credentials,SECRET_KEY,algorithms=[ALGORITHM])
     email : str = payload.get("sub")
     if email is None:
        raise credential_exception
    
    except JWTError:
         raise credential_exception
    
    return email 

