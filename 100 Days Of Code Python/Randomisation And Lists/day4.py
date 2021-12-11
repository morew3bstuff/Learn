# Module inports
from myModule import *

# Display imported variables
print(randomInt)
print(randomFloat)
print(randomFloat * 5)

# Coin Toss
if randomCoin == 1:
    print("Heads!")
else:
    print("Tails!")

# Lists
statesUs = ["Delaware", "Virginia", "Texas"]
print(statesUs[0])
# Last List Item
print(statesUs[-1])
print(statesUs[-2])
# Change List Value
statesUs[0] = "StateReplaced"
print(statesUs)
# Add Item To List
statesUs.append("NewStateAdded")
print(statesUs)
statesUs.extend(["Item1", "Item2", "Item3"])
print(statesUs)
print(statesUs[-1])

# Roulette
nameStr = input("Give me a list of names devided by ',': ")
nameList = nameStr.split(", ")
randomPersonIndex = random.randint(0, len(nameList) - 1)
print(f"{nameList[randomPersonIndex]} was picked and gets to pay everyones meal! ---> Index Solution")
print(f"{random.choice(nameList)} was picked and gets to pay everyones meal! ---> .choice() Solution")

vegetables = ["Kale", "Celery", "Potatos"]
fruits = ["Apples", "Grapes", "Cherries"]
nested = [vegetables, fruits]

print(nested)