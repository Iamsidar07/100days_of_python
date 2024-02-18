import turtle
import pandas

IMAGE = "blank_states_img.gif"
screen = turtle.Screen()
screen.title("U.S. States Game")

screen.addshape(IMAGE)
turtle.shape(IMAGE)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_list = []
is_game_on = True
score = 0
while len(guessed_list) <= 50:
    user_answer = screen.textinput(
        title=f"{score}/50 Guess the state", prompt="What's another state of USA? "
    ).title()
    if user_answer == "Exit":
        missed_states = [state for state in all_states if state not in guessed_list]
        # missed_states = []
        # for state in all_list:
        #     if state not in guessed_list:
        #         missed_states.append(state)
        df = pandas.DataFrame(missed_states)
        df.to_csv("states_to_learn.csv")
        break
    if user_answer in all_states:
        state_data = data[data.state == user_answer]
        guessed_list.append(user_answer)
        score += 1
        state_name = state_data.state.item()
        state_pos_x = int(state_data.x.iloc[0])
        state_pos_y = int(state_data.y.iloc[0])
        tim = turtle.Turtle()
        tim.shape("circle")
        tim.hideturtle()
        tim.penup()
        tim.goto(state_pos_x, state_pos_y)
        tim.write(state_name, align="center", font=("Courier", 12, "normal"))
