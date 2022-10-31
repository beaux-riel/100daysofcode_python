# Day 6 of 100 Days of Code - Python
# https://www.udemy.com/course/100-days-of-code/
# Exercise - Python Functions and Karel

# This unit wasn't as engaging as I would have liked. Plenty of other ways to make functions way more fun. Very "Swift Playgrounds".

# Assignment - Escaping the Maze - Reeborg's World
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while front_is_clear():
    move()
turn_left()
    
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()