from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500,height=400)
is_race_on = True
user_bet = screen.textinput(title="Welcome to the Turtle Race",
                         prompt="Which turtle will win the race? Enter a color: ").lower()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtle_list = []

def turtle_lineup(color, position_x, position_y):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[color])
    new_turtle.penup()
    new_turtle.goto(x=position_x, y=position_y)
    turtle_list.append(new_turtle)

y_first_turtle = 130

if user_bet in colors:
    is_race_on = True
    for a in range(6):
        turtle_lineup(color=a, position_x=-230, position_y=y_first_turtle)
        y_first_turtle -= 50
    while is_race_on:
        for turtle_racer in turtle_list:
            if turtle_racer.xcor() > 220:
                is_race_on = False
                winning_color = turtle_racer.pencolor()
                if user_bet == winning_color:
                    print(f"You've won! The {winning_color} turtle is the winner!")
                else:
                    print(f"You've lost! The {winning_color} turtle is the winner!")
            turtle_racer.forward(distance=random.randrange(0,10))
else:
    is_race_on = False


screen.exitonclick()

