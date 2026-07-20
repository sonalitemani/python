class Car:
    def __init__(self,brand ,model,year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def fullName(self):
        return f"{self.brand} {self.model} {self.year}"

myCar = Car('Toyota', 'Camry', 2024)
print(myCar.fullName())
