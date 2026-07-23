from pydantic import BaseModel , Field
from typing import Optional 

class Employee(BaseModel):
    id: int
    name: str = Field(
        ...,
        min_length=2 , 
        max_length=20 , 
        description='Employee name'
    )
    department: Optional[str] = None
    salary: float = Field(
        ...,
        ge=10000
    )
    