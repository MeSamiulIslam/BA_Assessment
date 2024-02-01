class Car:
    def __init__(self, name, model, year):
        self.name = name
        self.model = model
        self.year = year

    def display_info(self):
        return f"{self.year} {self.name} {self.model}"
class ElectricCar(Car):
    def __init__(self, name, model, year, battery_capacity):
        super().__init__(name, model, year)
        self.battery_capacity = battery_capacity

    def display_info(self):
        return f"{super().display_info()}\nBattery Capacity: {self.battery_capacity} kWh"

class GasCar(Car):
    def __init__(self, name, model, year, fuel_efficiency):
        super().__init__(name, model, year)
        self.fuel_efficiency = fuel_efficiency

    def display_info(self):
        return f"{super().display_info()}\nFuel Efficiency: {self.fuel_efficiency} MPG"
def main():
    car_type = input("Enter car type (Electric/Gas): ")
    name = input("Enter Name: ")
    model = input("Enter model: ")
    year = input("Enter year: ")

    if car_type.lower() == 'electric':
        battery_capacity = input("Enter battery capacity (kWh): ")
        car = ElectricCar(name, model, year, battery_capacity)
    elif car_type.lower() == 'gas':
        fuel_efficiency = input("Enter fuel efficiency (MPG): ")
        car = GasCar(name, model, year, fuel_efficiency)
    else:
        print("Invalid car type")

    print("Car Information:")
    print(car.display_info())

if __name__ == "__main__":
    main()
