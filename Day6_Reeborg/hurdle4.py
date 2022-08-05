"""  My Way Below *** Almost worked!***
Remember to know you can add while loop inside a function
When facing the turn left on jump() problem if there is no wall_on_right!

Refer to correct code below

def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    # move()
    turn_left()
    move()


while not wall_on_right():
    turn_right()
    move()
    if wall_in_front():
        jump()

while right_is_clear():
    turn_right()
    move()

while not at_goal():
    if wall_in_front():
        jump()
    elif right_is_clear():
        turn_right()
        move()
    else:
        move()

        """

# Below correct code


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()


while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()
