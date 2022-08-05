def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


for step in range(6):
    jump()

number_of_hurdles = 6
while number_of_hurdles > 0:
    jump()
    number_of_hurdles -= 1
    print(number_of_hurdles)

# To stop when reaching goal using pre built at_goal() function
while at_goal != True:
    jump()

# Using negation - opposite of "if condition is true "statement
while not at_goal():
    jump()

# def turn_around():
#     turn_left()
#     turn_left()

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# move()
# move()
# turn_left()
# move()
# turn_right()
# move()

# def draw_square():
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()

# draw_square()
