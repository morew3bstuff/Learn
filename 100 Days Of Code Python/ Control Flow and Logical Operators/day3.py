# if / else statement
print("Welcome to the rollercoaster!")
print("-" * 50)

# Inputs and Variables
height = int(input("What's your height in cm(eg: 175): "))

if height > 120:
    print("You can ride the rollercoaster.")
else:
    print("Come back next year.")
print()

# Odd or Even 
print("Odd or Even")
print("-" * 50)
number = int(input("Give me a number: "))
if number % 2 == 0:
    print(f"Given number {number} is even.")
else:
    print(f"Given number {number} is odd.")
print()

print("Nested if")
print("-" * 50)
if height > 120:
    age = int(input("What's your age: "))
    if age >= 18:
        print("You can ride the rollercoaster but you need to pay full price 12$.")
    else:
        print("You can ride the rollercoaster but you need to pay 8$.")
else:
    print("Come back next year.")
print()

print("elif")
print("-" * 50)
if height > 120:
    print("You can ride the rollercoaster.")
    age = int(input("What's your age: "))
    if age >= 18:
        print("Since your an adult you pay full price 12$.")
    elif age < 18:
        print("Since your not an adult you pay reduced price 8$.")
else:
    print("Come back next year.")
print()

print("BMI 2.0")
print("-" * 50)
weight = int(input("Your weight in kg: "))
height = float(input("Your height eg 175cm write 1.75: "))
bmi = round(weight / height ** 2, 2)

if bmi < 18.5:
    print(f"Your BMI is {bmi}, you're underweight.")
elif (bmi >= 18.5 and bmi < 25):
    print(f"Your BMI is {bmi}, you're normal weight.")
elif (bmi >= 25 and bmi < 30):
    print(f"Your BMI is {bmi}, you're overweight.")
elif (bmi >= 30 and bmi < 35):
    print(f"Your BMI is {bmi}, you're obese.")
elif bmi >35:
    print(f"Your BMI is {bmi}, you're clinically obese.")
print()

print("Leep year")
print("-" * 50)
year = int(input("What year fo you want to check: "))
if year % 4 == 0:
    if (year % 100 == 0 and year % 400 == 0):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")
else:
    print(f"{year} is not a leap year.")