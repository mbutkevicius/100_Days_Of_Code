print("Hello")
num_char = len("Hello")
print(num_char)

# Ctrl + ] will tab things to right. Ctrl + [ will tab to left


def my_function():
    print("Hello")
    print("Bye")


my_function()

# hurdles challenge:

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
# def jump():
#     while wall_on_right() == True:
#         move()
#     turn_right()
#     move()
#     turn_right()
#     while not wall_in_front():
#         move()
#     turn_left()
#
# while not at_goal():
#     if front_is_clear():
#         move()
#     elif wall_in_front():
#         turn_left()
#         jump()

# Maze challenge:
def turn_right():
    turn_left()
    turn_left()
    turn_left()


while not at_goal():
    if right_is_clear():
        if not front_is_clear():
            turn_right()
            move()
        else:
            move()
    elif wall_on_right() and front_is_clear():
        move()
    # I'm pretty sure this one is useless
    # elif front_is_clear():
    #     move()
    else:
        turn_left()
