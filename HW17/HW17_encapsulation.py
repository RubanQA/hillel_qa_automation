class Car:
    def __init__(self, brand, model, engine, drive, fuel, color, price):
        self.brand = brand
        self.model = model
        self.engine = engine
        self.drive = drive
        self.fuel = fuel
        self.color = color
        self.__price = price
        self.__discount = None

    def set_discount(self, discount):
        self.__discount = discount

    def get_price(self):
        if self.__discount:
            return self.__price * (1 - self.__discount)
        return self.__price

    def __repr__(self):
        return f'Brand: {self.brand}, Model: {self.model}, Engine: {self.engine}, Drive: {self.drive}, Fuel: {self.fuel}, '\
               f'Color: {self.color},Price: {self.get_price()}'


car1 = Car("BMW", "320", 2.0, "RWD", "Petrol", "Black", 27.000)
car2 = Car("Audi", "A6", 1.8, "AWD", "Diesel", "White", 30.000)
car3 = Car("Porsche", "Panamera",  3.0, "FWD", "Electric", "Gold", 120.000)
car1.set_discount(0.20)
car2.set_discount(0.30)
car3.set_discount(0.50)

if __name__ == '__main__':
    print(car1.get_price())
    print(car2.get_price())
    print(car3.get_price())
    print(car1)
    print(car2)
    print(car3)