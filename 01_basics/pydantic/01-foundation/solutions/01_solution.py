from pydantic import  BaseModel

class Product(BaseModel):
    id: int
    price: float
    name: str
    in_stock: bool = True