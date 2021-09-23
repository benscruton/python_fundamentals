# Create a class called  Car. In the__init__(), allow the user to specify the following attributes: price, speed, fuel, mileage. If the price is greater than 10,000, set the tax to be 15%. Otherwise, set the tax to be 12%. 

# Create six different instances of the class Car. In the class have a method called display_all() that returns all the information about the car as a string. In your __init__(), call this display_all() method to display information about the car once the attributes have been defined.


class Car:
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.tax = 0.15 if price > 10000 else 0.12
        self.display_all()

    def display_all(self):
        info  = f"Price:   ${self.price}\n"
        info += f"Speed:   {self.speed} mph\n"
        info += f"Fuel:    {self.fuel}\n"
        info += f"Mileage: {self.mileage}\n"
        info += f"Tax:     {self.tax}\n"
        print(info)

car1 = Car(11000, 90, 12, 40000)
car2 = Car(23000, 110, 14, 1000)
car3 = Car(7500, 90, 10, 120000)
car4 = Car(6000, 85, 12, 160000)