from uuid import UUID
from datetime import date, datetime
from typing import Optional, List

#Pydantic
from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import Field

#Fast API
from fastapi import FastAPI, HTTPException
from fastapi import status

app = FastAPI()

#MODELS
class UserBase(BaseModel):
    user_id : UUID = Field()
    mail : EmailStr = Field()
class UserLogin(UserBase):
    password : str  = Field(
        ..., 
        min_length=8,
        max_length=64
        )
class User(UserBase):
    username : str = Field(
        ...,
        min_length=1,
        max_length=20
    )
    birth_date: Optional[date] = Field(default=None)
class Tweet(BaseModel):
    tweet_id : UUID = Field()
    content : str = Field(
        ...,
        max_length=256,
        min_length=1
    )
    created_at : datetime = Field(default=datetime.now())
    updated_at : Optional[datetime] = Field(default=None)
    by : User = Field()

#Path operations

@app.get(path="/")
def home():
    return {"Twitter API" : "Working!"}

##Users

@app.post(
    path="/signup",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary= "Register a user",
    tags= ["Users"]
    )
def signUp():
    pass

@app.post(
    path="/login",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary= "Login a user",
    tags= ["Users"]
    )

def logIn():
    pass

@app.get(
    path="/users",
    response_model=List[User],
    status_code=status.HTTP_200_OK,
    summary= "Show all users",
    tags= ["Users"]
    )
def show_all_users():
    pass
@app.get(
    path="/users/{user_id}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary= "Show a user",
    tags= ["Users"]
    )
def show_a_user():
    pass

@app.delete(
    path="/users/{user_id}/delete",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary= "Delete a user",
    tags= ["Users"]
    )
def delete_a_user():
    pass

@app.put(
    path="/users/{user_id}/update",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary= "Update a user",
    tags= ["Users"]
    )
def update_a_user():
    pass

##Tweets