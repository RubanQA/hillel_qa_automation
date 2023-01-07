from abc import ABC, abstractmethod


class Car:
    def __init__(self, brand, model, engine, drive, fuel, color, price):
        self.brand = brand
        self.model = model
        self.engine = engine
        self.drive = drive
        self.fuel = fuel
        self.color = color
        self.price = price
        self.discount = None

    def set_discount(self, discount):
        self.discount = discount

    def get_price(self):
        if self.discount:
            return self.price * (1 - self.discount)
        return self.price

    @abstractmethod
    def __repr__(self):
        pass


class FireTruck(Car):
    def __init__(self, brand, model, engine, drive, fuel, color, price, status):
        super().__init__(brand, model, engine, drive, fuel, color, price)
        self.status = status

    def __repr__(self):
        return f'Brand: {self.brand}, Model: {self.model}, Engine: {self.engine}, Drive: {self.drive}, Fuel: {self.fuel}, ' \
               f'Color: {self.color}, Price: {self.get_price()}, Status: {self.status}'


class RacerCar(Car):
    def __init__(self, brand, model, engine, drive, fuel, color, price, turbo):
        super().__init__(brand, model, engine, drive, fuel, color, price)
        self.turbo = turbo

    def __repr__(self):
        return f'Brand: {self.brand}, Model: {self.model}, Engine: {self.engine}, Drive: {self.drive}, Fuel: {self.fuel}, ' \
               f'Color: {self.color}, Price: {self.get_price()}, Turbo: {self.turbo}'


fire_truck1 = FireTruck("Man", "Fire Truck", 6.0, "FWD", "Diesel", "Red", 120.000, "Special")
racer_car1 = RacerCar("Lamborgini", "Diablo", 4.0, "AWD", "Petrol", "Red", 500.000, "Biturbo")
fire_truck1.set_discount(0.20)
racer_car1.set_discount(0.30)
print(fire_truck1)
print(racer_car1)
