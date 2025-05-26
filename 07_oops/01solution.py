class Car():
    total_Car = 0

    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.total_Car += 1

    def get_brand(self):
        return self.__brand + "!"

    def fullName(self):
        return f"{self.__brand} {self.__model}"

    def fuel_type(self):
        return "Petrol or Diesel"   

    @staticmethod
    def desc():
        return "cars are good and awesome."
    
    @property
    def model(self):
        return self.__model
        

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric charge"

# myelectCar = ElectricCar("Tesla","M2","100kWh")

# print(isinstance(myelectCar,Car))
# print(isinstance(myelectCar,ElectricCar))

# print(myelectCar.brand)
# print(myelectCar.get_brand())
# print(myelectCar.fuel_type())

# mycar = Car("Tata","Curve")
# Car("Tata","Harrier")
# print(mynewCar.fuel_type())
# print(Car.total_Car)
# print(mycar.desc())
# print(Car.desc())
# mycar.model = "Hexa"
# print(mycar.model)

# myCollect = Car("Tata","Curve")
# print(myCollect.brand)
# print(myCollect.fullName()) 


class battery:
    def battery_info(self):
        return "this is a battery"

class engine:
    def engine_info(self):
        return "this is a engine"

class ElectricCarTwo(battery,engine):
    pass

mynewTata = ElectricCarTwo()
print(mynewTata.battery_info())
print(mynewTata.engine_info())