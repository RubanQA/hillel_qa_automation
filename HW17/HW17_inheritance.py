class Car:
    def __init__(self, brand, model, engine, drive, fuel, color, price):
        self.brand = brand
        self.model = model
        self.engine = engine
        self.drive = drive
        self.fuel = fuel
        self.color = color
        self.price = price

    def __repr__(self):
        return f'Brand: {self.brand}, Model: {self.model}, Engine: {self.engine}, Drive: {self.drive}, Fuel: {self.fuel}, ' \
               f'Color: {self.color}, Price: {self.price}'


class FireTruck(Car):
    def __init__(self, brand, model, engine, drive, fuel, color, price, status):
        super().__init__(brand, model, engine, drive, fuel, color, price)
        self.status = status

    def __repr__(self):
        return f'Brand: {self.brand}, Model: {self.model}, Engine: {self.engine}, Drive: {self.drive}, Fuel: {self.fuel}, ' \
               f'Color: {self.color}, Price: {self.price}, Status: {self.status}'


class RacerCar(Car):
    def __init__(self, brand, model, engine, drive, fuel, color, price, turbo):
        super().__init__(brand, model, engine, drive, fuel, color, price)
        self.turbo = turbo

    def __repr__(self):
        return f'Brand: {self.brand}, Model: {self.model}, Engine: {self.engine}, Drive: {self.drive}, Fuel: {self.fuel}, ' \
               f'Color: {self.color}, Price: {self.price}, Turbo: {self.turbo}'


fire_truck1 = FireTruck("Man", "Fire Truck", 6.0, "FWD", "Diesel", "Red", 120.000, "Special")
racer_car1 = RacerCar("Lamborgini", "Diablo", 4.0, "AWD", "Petrol", "Red", 500.000, "Biturbo")
print(fire_truck1)
print(racer_car1)
