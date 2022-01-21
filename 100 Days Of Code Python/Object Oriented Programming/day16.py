from turtle import Turtle, Screen
from prettytable import PrettyTable

slow_poke = Turtle()
my_screen = Screen()
x = PrettyTable()

# my_screen.canvheight = 100
# my_screen.canvwidth = 100
slow_poke.shape("turtle")
slow_poke.color("Dark Green")
slow_poke.forward(100)
my_screen.exitonclick()

x.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
x.add_row(["Adelaide", 1295, 1158259, 600.5])
x.add_row(["Brisbane", 5905, 1857594, 1146.4])
x.add_row(["Darwin", 112, 120900, 1714.7])
x.add_row(["Hobart", 1357, 205556, 619.5])
x.add_row(["Sydney", 2058, 4336374, 1214.8])
x.add_row(["Melbourne", 1566, 3806092, 646.9])
x.add_row(["Perth", 5386, 1554769, 869.4])

# print(slow_poke)
# print(my_screen.canvwidth)
print(x)



