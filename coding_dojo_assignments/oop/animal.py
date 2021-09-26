class Animal:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def walk(self):
        self.health -= 1
        return self

    def run(self):
        self.health -= 5
        return self

    def display_health(self):
        print(f"\n{self.name}'s Health: {self.health}")
        return self
    
a1 = Animal("Fido", 100)
a1.display_health().walk().walk().walk().run().run().display_health()

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, 150)

    def pet(self):
        self.health += 5
        return self

d1 = Dog("Steve")
print(d1.name)
d1.display_health().pet().pet().display_health()

class Dragon(Animal):
    def __init__(self, name):
        super().__init__(name, 170)

    def fly(self):
        self.health -= 10
        return self
    
    def display_health(self):
        super().display_health()
        print("I AM DAGRON")
        return self

d2 = Dragon("Trogdor the Burninator")
d2.fly().display_health().fly().display_health()

a2 = ("Not a dragon", 22)

try:
    a2.fly()
except:
    print("Only dragons can fly.")

try:
    a2.pet()
except:
    print("Only dogs get pets.")

try:
    d1.fly()
except:
    print("Dogs cannot fly.")