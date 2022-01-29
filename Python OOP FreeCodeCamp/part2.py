import csv

# Create the class
class Item():
    pay_rate = 0.8 # Class attribute
    all = []
    # Constructor method, gets called automaticaly when creating an instace of a class
    def __init__(self, name: str, price: float, quantity=0): # quantity default to 0, not a mandatory argument
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater or equal to 0."
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to 0."

        # Assign to self object
        self.name = name # Dynamic attribute assignment
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate # self.pay_rate, self allows to change the pay_rate at the instance level

    def __repr__(self): # The way instances of a class are represented on print
        return f'Item({self.name}, {self.price}, {self.quantity})'

item1 = Item("Phone", 100, 5)
item2 = Item("Laptop", 1000, 3)

print(f"{item1.name}, {item1.price}, {item1.quantity}   <--- print(item1.name, item1.price, item1.quantity)")
print(f"{item2.name}, {item2.price}, {item2.quantity} <--- print(item2.name, item2.price, item2.quantity)")

total_price1 = item1.calculate_total_price()
total_price2 = item2.calculate_total_price()

print("\n")
print(f"{total_price1}  <--- total_price1 = item1.calculate_total_price()")
print(f"{total_price2} <--- total_price2 = item2.calculate_total_price()")

print("\n")
print(Item.pay_rate)
print(item1.pay_rate)

print("\n")
print("Display all attributes.")
print("-" * 23)
print(Item.__dict__) # All the attributes for the class level
print("\n")
print(item1.__dict__) # All the attributes for the instance level

print("\n")
print(f"item1 full price {item1.price}.")
item1.apply_discount()
print(f"item1 discount price {item1.price}.")

print("\n")
item2.pay_rate = 0.7 # Overide the discount just for item 2
print(f"item2 full price {item2.price}.")
item2.apply_discount()
print(f"item2 discount price {item2.price}.")
print("\n")

# Recrete instances
item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)

print(Item.all)