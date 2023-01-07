from HW17_encapsulation import Car


class FireTruck(Car):
    def __init__(self, brand, model, engine, drive, fuel, color, price, status):
        super().__init__(brand, model, engine, drive, fuel, color, price)
        self.status = status


class RacerCar(Car):
    def __init__(self, brand, model, engine, drive, fuel, color, price, turbo):
        super().__init__(brand, model, engine, drive, fuel, color, price)
        self.turbo = turbo

    def __repr__(self):
        return f'{super().__repr__()}, Turbo: {self.turbo}'


fire_truck1 = FireTruck("Man", "Fire Truck", 6.0, "FWD", "Diesel", "Red", 120.000, "Special")
racer_car1 = RacerCar("Lamborgini", "Diablo", 4.0, "AWD", "Petrol", "Red", 500.000, "Biturbo")
print(fire_truck1)
print(racer_car1)
