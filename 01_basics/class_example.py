class Car:
    total_cars = 0
    def __init__(self,brand ,model,year):
        self.brand = brand
        self.model = model
        self.year = year
        Car.total_cars +=1
    
    def fullName(self):
        return f"{self.brand} {self.model} {self.year}"

class ElectricCar(Car):
    def __init__(self,brand,model,year,battery):
        super().__init__(brand,model,year)
        self.battery = battery

myECar = ElectricCar('TTT','2222','2922','85KWH')
print(myECar.fullName())

myCar = Car('Toyota', 'Camry', 2024)
print(myCar.fullName())
print(myCar.total_cars)
