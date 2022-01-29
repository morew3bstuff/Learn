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

    @classmethod # Decorator to create a class method
    def instantiate_from_csv(cls): # Class obj itself is passed as the 1st argument
        with open('sample.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name = item.get('Name'),
                price = float(item.get('Price')),
                quantity = float(item.get('Quantity'))
            )

    @staticmethod
    def is_integer(num):
      if isinstance(num, float):
        return num.is_integer()
      elif isinstance(num, int):
        return True
      else:
        return False

    def __repr__(self): # The way instances of a class are represented on print
        return f'Item({self.name}, {self.price}, {self.quantity})'


Item.instantiate_from_csv()
print(Item.all)
print('\n')

print(Item.is_integer(5.1))