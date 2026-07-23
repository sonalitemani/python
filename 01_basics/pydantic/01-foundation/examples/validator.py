from pydantic import field_validator , model_validator ,computed_field ,BaseModel

class User(BaseModel):
    username: str

    @field_validator('username')
    def username_length(cls, v):
        if len(v) < 4:
            raise ValueError('Username must be at least 4 characters long')
        return v

class Signup(BaseModel):
    password: str
    confirm_password: str

    @field_validator('password','confirm_password')
    def pass_length(cls, v):
        if len(v) < 8:
            raise ValueError('Password must be at least 8 characters long')
        return v

    @model_validator(mode='after')
    def check_password_match(self):
        if self.password != self.confirm_password:
            raise ValueError('Passwords do not match')
        return self

class Product(BaseModel):
    price: float
    quantity: int

    @computed_field
    @property
    def total_price(self) -> float:
        return self.price * self.quantity
    

product = Product(price=10 , quantity=2)

print(product.total_price)

username = User(username="sao123")

print(username)

password = Signup(password='password', confirm_password='password')

print(password)

