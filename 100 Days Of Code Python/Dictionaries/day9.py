dict = {"Bug" : "An error in a program.", "Function" : "A piece of code that you can call over again and again."}

print(dict)
print()
print(dict["Bug"])
print()

dict["Loop"] = "The action of doing something over and over."
print(dict)
print()

for item in dict:
    print(item)
print()

# Ex 1
scores = {
    "Harry" : 81, 
    "Ron" : 78, 
    "Maria" : 44, 
    "Sam" : 99, 
    "Nelly" : 82
}
print(scores)
print()

grades = {}
for item in scores:
    mark = scores[item]
    if mark >= 91:
        grades[item] = "Outstanding"
    elif mark >= 81 and mark < 91:
        grades[item] = "Exceeds Expectation"
    elif mark >= 71 and mark < 81:
        grades[item] = "Acceptable"
    elif mark < 70:
        grades[item] = "Fail"
print(grades)
print()

capitals = {
    "France" : "Paris",
    "Germany" : "Berlin"
}

travel = {
    "France" : ["Paris", "Lille", "Dijon"],
    "Germany" : ["Berlin", "Hamburg", "Stuttgard"]
}
print(capitals)
print()
print(travel)

travel = {
    "France" : {"visited" : ["Paris", "Lille", "Dijon"], "visits" : 12},
    "Germany" : ["Berlin", "Hamburg", "Stuttgard"]
}
print(travel)
print()

travel_log = [
    {
        "country" : "France",
        "cities" : ["Paris", "Lille", "Dijon"],
        "visits" : 12
    },
    {
        "country" : "Germany",
        "cities" : ["Berlin", "Hamburg", "Stuttgard"],
        "visits" : 5
    }
] 

for item in travel_log:
    print(item)
print()

# Ex 2
def add_entry(country, cities, visists):
    travel_log.append(
        {
            "country" : country,
            "cities" : cities,
            "visits" : visists
        }
    )
add_entry(country="Rusia", cities=["Moscow", "Saint Petersburg"], visists=9)
print(travel_log)