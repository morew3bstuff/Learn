# Starter
item1 = "Phone"
item1_price = 100
item1_quantity = 5
item1_price_total = item1_price * item1_quantity

print("Everything in Python is an object!")
print("-" * 34)
print("\n")

print(f'item1 = "Phone"                                  <--- Type: {type(item1)}')
print(f'item1_price = 100                                <--- Type: {type(item1_price)}')
print(f'item1_quantity = 5                               <--- Type: {type(item1_quantity)}')
print(f'item1_price_total = item1_price * item1_quantity <--- Type: {type(item1_price_total)}')

print("\n")
print("-" * 144)
print("\n")

# Dummy Class
print("Create a dummy class.")
print("-" * 21)
print("\n")
print(f"class Item(): \n" + f"    pass")

class Item():
    def calculate_total_price(self, x, y):
        return x * y

print("\n")
print("Create instance of class Item().")
print("-" * 32)
print("item2 = Item()")
print("")

print("\n")
print("Assign attributes to class Item().")
print("-" * 34)
print('item2.name = "Phone"')
print('item2.price = 100')
print('item2.qunatity = 5')

item2 = Item()
item2.name = "Laptop"
item2.price = 1000
item2.quantity = 3

print("\n")
print("Type of Item() and it's attributes.")
print("-" * 35)
print(f'item2 <--- {type(item2)}')
print(f'item2.name <--- {type(item2.name)}')
print(f'item2.price <--- {type(item2.price)}')
print(f'item2.quantity <--- {type(item2.quantity)}')

print("\n")
print("Add a method to a class.")
print("-" * 24)
print("\n")
print(f"class Item(): \n" + f"    def calculate_total_price(self, x, y): \n" + f"        return x * y")

print("\n")
print("Call the method.")
print("-" * 16)
print(f"item2.calculate_total_price(item2.price, item2.quantity)")

print("\n")
print("Can save method return in another variable.")
print("-" * 43)
print(f"result = item2.calculate_total_price(item2.price, item2.quantity)")
result = item2.calculate_total_price(item2.price, item2.quantity)
print(f"{result} <--- print(result)")