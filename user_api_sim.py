users = []

choice = "yes"

def create_user(a,b):
    id = len(users)+1
    d = {"id":id,"name":a,"email":b}
    users.append(d)
    out_put = {
    "status_code" : 201,
    "message": "user created successfully",
    "data":users
 }
    return out_put


while choice == "yes":
  
  a = input("Enter your Name :")
  b = input("Enter your Email: ")
  responce = create_user(a,b)
  print(responce)
  
  choice =input("do u want to add more user :").lower()

given_id = int(input("which user id u want to deleat 1 , 2  , 3 , 4 or 5  = "))

def delete_user_id(given_id) :
   for x in users:
  
    if x["id"]==given_id:
      
      print("user found ")
      print(x)
      users.remove(x)
      out_put_2 = {
    "status_code" : 200,
    "message": "user removed successfully",
    "data":users
 }
      return out_put_2
   return {
        "status_code": 404,
        "message": "user not found"
    }
 
   
rsponce_2 = delete_user_id(given_id)  
print(rsponce_2)
    

def get_users():
    get_data = {
    "status_code" : 200,
    "massage": "all users listed succesfully",
    "data":users
    }


    return get_data

x= get_users()
print(x)
