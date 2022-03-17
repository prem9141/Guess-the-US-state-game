from turtle import Turtle, Screen
import pandas as pd

MOVE = False
ALIGN = "center"
FONT = ('Courier', 7, 'bold')

IMAGE_PATH = './blank_states_img.gif'
user_score = 0
user_state_input = ''

screen = Screen()
screen.title("Name the States")
screen.addshape(IMAGE_PATH)

map_image = Turtle()
map_image.shape(IMAGE_PATH)


state = Turtle()
state.hideturtle()
state_list = pd.read_csv('./50_states.csv')
state_list['state'] = state_list['state'].str.lower()

user_state_input = screen.textinput(title=f"Guess the State", prompt="Enter the state name")

while user_state_input is not None:
    user_state_input = user_state_input.lower().strip()

    df = state_list[state_list['state'] == user_state_input]

    if len(df) > 0:
        user_score += 1
        state.penup()
        state.goto(df.x.item(), df.y.values[0])
        state.pendown()
        state.write(df.state.values[0], MOVE, ALIGN, FONT)

    if user_score == 0:
        user_state_input = screen.textinput(title=f"Guess the State", prompt="Enter the state name")
    else:
        user_state_input = screen.textinput(title=f"{user_score}/50 States Correct",
                                            prompt="What's another state name?")
screen.exitonclick()
