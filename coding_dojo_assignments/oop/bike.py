class Bike:
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    def __repr__(self):
        return f"This bike costs ${self.price}."
    
    def displayInfo(self):
        print()
        print(f"Price:     {self.price}")
        print(f"Max speed: {self.max_speed}")
        print(f"Mileage:   {self.miles}")
        print()
        return self

    def ride(self, distance = 10):
        self.miles += distance
        return self

    def reverse(self, distance = 5):
        self.miles -= distance
        return self

bike1 = Bike(200, 45)
bike1.ride()        # miles: 10
bike1.ride(20)      # miles: 30
bike1.ride()        # miles: 40
bike1.reverse()     # miles: 35
bike1.ride(7)       # miles: 42
bike1.displayInfo()

bike2 = Bike(175, 40)
bike2.ride().ride().ride().ride().reverse(2).displayInfo()  # miles: 38

# testing __repr__ function:
print(bike1)
print(bike2)