# Assignment: Product
# The owner of a store wants a program to track products. Create a product class to fill the following requirements.

# Product Class:
    # Attributes:
        # Price • Item Name • Weight • Brand • Status: default "for sale"

    # Methods:
        # • Sell: changes status to "sold"
        # • Add tax: takes tax as a decimal amount as a parameter and returns the price of the item including sales tax
        # • Return: takes reason for return as a parameter and changes status accordingly. If the item is being returned because it is defective, change status to "defective" and change price to 0. If it is being returned in the box, like new, mark it "for sale". If the box has been, opened, set the status to "used" and apply a 20% discount.
        # • Display Info: show all product details.
class Product:
    def __init__(self, price, item_name, weight, brand):
        self.price = price
        self.name = item_name
        self.weight = weight
        self.brand = brand
        self.status = "For sale"
        return self

    def sell(self):
        self.status = "Sold"
        return self

    def add_tax(self, tax_percentage):
        return self.price * tax_percentage

    def return_product(self, reason, like_new = False):
        if reason.lower() == "defective":
            self.price = 0
            self.status = "defective"
        elif like_new:
            self.status = "For sale"
        else:
            self.status = "Used"
            self.price *= 0.8
        return self

    def display_info(self):
        output  = f"Price:     {self.price}"
        output += f"Item name: {self.name}"
        output += f"Weight:    {self.weight}"
        output += f"Brand:     {self.brand}"
        output += f"Status:    {self.status}"
        print(output)
        return self