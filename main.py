import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)

screen.tracer(0)

writer = turtle.Turtle()
writer.penup()
writer.hideturtle()

state_list = pandas.read_csv("50_states.csv")

list_state_list = state_list["state"].to_list()

guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}'/50' Guess the state", prompt="What's another state's name").title()
    if answer_state == "Exit":
        break
    if answer_state in list_state_list:
        if answer_state not in guessed_states:
            row = state_list[state_list["state"] == answer_state]
            writer.goto(int(row.x), int(row.y))
            writer.write(answer_state,align="center",font=("Courier", 8, "normal"))
            guessed_states.append(answer_state)

# Save remaining states to states to learn.csv
copy_state_list = list_state_list
for state in guessed_states:
    copy_state_list.remove(state)

df = pandas.DataFrame(copy_state_list)
df.to_csv("states to learn.csv")