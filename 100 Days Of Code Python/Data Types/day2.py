print("Data Types")
print("-" * 100)

# String
print("%s %s" % ("Hello", "String"))
print("%s %s" % ("Hello"[0], "Hello[0]")) # Index; Subscripting
print("%s %s" % ("Hello"[4], "Hello[4]")) 

# Integer
print("%s %s" % (123, "Integer"))
print("%s %s" % (123_245_332, "123_245_332"))

# Float
print("%s %s" % (5.22, "Float"))

# Boolean
print("%s %s" % (True, "Boolean"))
print("%s %s" % (False, "Boolean"))

num_ex = 7
print("%s %s" % (type(num_ex), "Type of number 7"))
print()

# TypeCasting
num_char = len(input("Your name: "))
print("Your name has " + str(num_char) + " characters.")
print()

print("%s %s" % ((70 + float("100.5")), """||| 70 + float("100.5")"""))
print("%s %s" %("70" + "1101", "||| 70 + 1101"))
print()

# Ex 1 - Add indexs of two digit "number"
print("""Ex 1 - Add indexs of two digit "number""")
inputNo = input("Provide two digit number: ")
first = int(inputNo[0])
second = int(inputNo[1])
print(first + second)
print()

# Math
print("%s %s" % (7 + 3, "7 + 3"))
print("%s %s" % (7 * 3, "7 * 3"))
print("%s %s" % (7 - 3, "7 - 3"))
print("%s %s" % (7 / 3, "7 / 3"))
print("%s %s" % (7 ^ 3, "7 ^ 3"))
print("%s %s" % (7 ** 3, "7 ** 3"))
print()

print("%s %s" % (3 * 3 + 3 / 3 - 3, "||| (3 * 3 + 3 / 3 - 3)"))
print()

# Ex 2 - BMI Calculator
print("Ex 2 - BMI Calculator")
print("-" * 100)
import math
height = float(input("Give me your height eg: 170cm enter 1.7: "))
weight = float(input("Give me your weight in kg: "))

bmi = weight / height ** 2
bmi_floor = math.floor(weight / height ** 2)

print("Your rounded BMI: %s." % (bmi_floor))
print("Real BMI: %s." % (bmi))
print(f"Your weight is: {weight}, your height is: {height} thus your bmi is: {bmi}.")
print()

# Ex 3 - Life in months, weeks and days 
print("Ex 3 - Life in month, weeks and days")
print("-" * 100)
age = int(input("Enter your age: "))
limit = 90
yearsLeft = limit - age
daysLeft = yearsLeft * 365
weeksLeft = round(yearsLeft * 52, 2)
monthsLeft = round(yearsLeft * 12, 2)
print(f"If you were to hit 90 you have {monthsLeft} months, {weeksLeft} weeks or {daysLeft} to go.")