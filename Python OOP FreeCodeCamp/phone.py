class Phone(Item):
  # Constructor method, gets called automaticaly when creating an instace of a class
  def __init__(self, name: str, price: float, quantity=0, broken_phone=0): # quantity default to 0, not a mandatory argument
    # Call to super function to have access to all attributes/methods of the parent class
    super().__init__(
      name, price, quantity
    )

    # Run validations to the received arguments
    assert broken_phone >= 0, f"Broken phone {broken_phone} is not greater or equal to 0."

    # Assign to self object
    self.broken_phone = broken_phone