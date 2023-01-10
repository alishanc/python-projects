from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ["Aazam", "Ali", "Mom"])
table.add_column("Type", ["Water", "Electric", "Wind"])

table.align = "l"

print(table)

# importing module and assigning class
import turtle
timmy = turtle.Turtle()

# import the module from the class and assign to object
from turtle import Turtle, Screen
timmy = Turtle()
print(timmy)
def square():
    global timmy
    timmy.shape("turtle")
    timmy.color("coral")
    timmy.forward(100)
    timmy.right(90)
    timmy.forward(100)
    timmy.right(90)
    timmy.forward(100)
    timmy.right(90)
    timmy.forward(100)
square()

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()



