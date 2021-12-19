# greet() function
def greet():
    print("You")
    print("are")
    print("late!")
greet()
print()

# greet2() function
def greet2(name):
    print(f"Hello {name}, you are late!")
greet2("Duke")
print()

# Functions with more than 1 parameter
def multi(name, greet):
    print(f"{greet} {name}, you are late!")
multi("Hi", "Sam")

# Keyword arguments
def keyWord(name, age):
    print(f"{name} is {age} years old.")
keyWord(age=23, name="Duke")

# Area Paint Calculator
# Need ceil because we can't buy half a can of paint
import math

# Asking the user for width, height and coverage per can
width = float(input("Give me the width: "))
heigth = float(input("Give me the heigth: "))
coverage = float(input("How much coverage do you get per can: "))

def calculatePainArea(width, height, coverage):
    # Calculation
    numberOfCansNeeded = math.ceil((width * heigth) / coverage)
    # Output
    print(f"You would need {numberOfCansNeeded} of cans to cover that area!")

calculatePainArea(width=width, height=heigth, coverage=coverage)

# Prime number checker
number = int(input("Give me a number: "))
# Function definition
def primeChecker(number):
    if (number % 2 != 0) and (number % 3 != 0) and (number % 5 != 0) and (number % 7 != 0) and (number % 6 != 0):
        print(f"Given number {number} is prime.")
    else:
        print(f"Given number {number} is not prime.")
# Function call, pass-in user given number
primeChecker(number=number)
