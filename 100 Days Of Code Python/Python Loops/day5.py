fruits = ["Apple", "Peach", "Pear"]

for fruit in fruits:
    print(fruit)
    print(fruit + " Pie.")
print()

# Average Height
studentHeights = [180, 124, 165, 173, 194, 169, 146]
totalHeight = 0
students = 0

for studentHeight in studentHeights:
    totalHeight += studentHeight

for student in studentHeights:
    students += 1

print(f"There are {students} students.")
print(f"Student heights: {studentHeights}.")
print(f"Average height is: {int(totalHeight / students)}.")
print()

# High Score
studentScores = [78, 65, 89, 86, 55, 91, 64, 89]
highScore = 0

for score in studentScores:
    if score > highScore:
        highScore = score

print(f"Student scores: {studentScores}.")
print(f"Highest score is: {highScore}.")
print()

total = 0

for number in range(1, 101):
    total += number
print(f"Gaus: {total}.")

total = 0

for number in range(1, 101):
    if number % 2 == 0:
        total += number
print(f"Gaus with even numbers: {total}.")

total = 0

for number in range(2, 101, 2):
    total += number
print(f"Gaus with even numbers, just range function: {total}.")