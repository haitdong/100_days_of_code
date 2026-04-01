from turtle import Turtle, Screen
import pandas as pd
df = pd.read_csv("50_states.csv")
import time

STATES = df.state.tolist()
LOWER_STATES = [state.lower() for state in STATES]
FONT = ("Courier", 10, "bold")

#initial screen setup
s = Screen()
s.setup(width=700, height=500)
s.addshape("blank_states_img.gif")
t = Turtle()
t.shape("blank_states_img.gif")
s.tracer(0)


correct_guess = []
game_on = True
while game_on:
    user_a = s.textinput(title=f"{len(correct_guess)}/50 States Correct", prompt="Name a state").title()
    s.update()
    time.sleep(0.1)
    if user_a in STATES and user_a not in correct_guess:
        guess = df[df.state == user_a]
        guess_x = guess.iat[0,1]
        guess_y = guess.iat[0,2]
        tim = Turtle()
        tim.penup()
        tim.hideturtle()
        tim.goto(guess_x, guess_y)
        tim.write(user_a, move=False, align="center", font=FONT)
        correct_guess.append(user_a)
    if len(correct_guess) == 50:
        game_on = False
        print("You win!")
    if user_a == "Exit":
        diff = list(set(STATES) - set(correct_guess))
        with open("states_left.csv", "w") as r:
            for item in diff:
                r.write(f"{item}\n")
        game_on = False

s.exitonclick()

