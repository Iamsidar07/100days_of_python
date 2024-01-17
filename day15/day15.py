# Object Oriented Programming

# from turtle import Turtle, Screen
#
# timmy = Turtle()
#
# timmy.shape("turtle")
# timmy.color("red")
# timmy.forward(100)
# my_screen = Screen()
#
# print(my_screen.window_height())
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.title = "Pokemon Park"
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table)
