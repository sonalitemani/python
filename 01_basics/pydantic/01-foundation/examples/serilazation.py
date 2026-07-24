from pydantic import BaseModel,ConfigDict
from typing import List 
from datetime import datetime

class Address(BaseModel):
    street:str
    city:str
    state:str
    zip:str
    country:str

class User(BaseModel):
    id:int
    name:str
    email:str
    is_active:bool=True
    createdAt:datetime
    address:Address
    tags: List[str] = []

    model_config = ConfigDict(
       json_encoders={datetime: lambda v: v.strftime("%Y-%m-%d %H:%M:%S")}
    )

user = User(
    id=1,
    name="John Doe",
    email="e@gmail.com",
    is_active=True,
    createdAt=datetime.now(),
    address=Address(
        street="123 Main St",
        city="New York",
        state="NY",
        zip="10001",
        country="USA"
    ),
    tags=["python", "pydantic"]
)
# we can convert model to dictionary using model_dump()
dict_data = user.model_dump()
print(dict_data)
print("--------------------------------------------------\n")
# using model dump_json() method we can convert model to json
json_data = user.model_dump_json(indent=4)
print(json_data)