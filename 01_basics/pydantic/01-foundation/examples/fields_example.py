from pydantic import BaseModel
from typing import List ,Dict ,Optional

class Cart(BaseModel):
    user_id: int
    items: List[str]
    discount: Dict [str , int]



    