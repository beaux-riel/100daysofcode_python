import turtle
import pandas

screen = turtle.Screen()
screen.title("Divided States of America")
image = "day25/us-states-game-start/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("day25/us-states-game-start/50_states.csv")
all_states = data.state.to_list()
guessed_states = []


while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", 
    prompt="What's another state's name?").title()
    print(answer_state)

#If answer_state is one of the states in all the states of the 50_states.csv
    #If they got it right:
    #Create a turtle to write the name of the state at the state's x and y coordinates

    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("day25/us-states-game-start/states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

# states_to_learn.csv