import turtle
from turtle import Turtle, Screen
import time
from paddle import Comp, Player
from ball import Ball

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 500
PADDLEL = 80
PADDLEW = 20
FONT = ("Courier", 40, "normal")

screen = Screen()
screen.setup(width=SCREEN_WIDTH,height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.tracer(0)
screen.listen()

comp = Comp()
player = Player()
ball = Ball()

screen.onkeypress(fun=player.move_up, key="w")
screen.onkeypress(fun=player.move_down, key="s")

#screen setup
splitter = Turtle()
splitter.color("white")
splitter.penup()
splitter.goto(x=0, y=250)
splitter.setheading(270)
splitter.pendown()
for a in range(13):
    splitter.forward(20)
    splitter.penup()
    splitter.forward(20)
    splitter.pendown()

#p score board
c_score = Turtle()
c_score.color("white")
c_score.penup()
c_score.hideturtle()
c_score.goto(x=40, y=180)
c_score.setheading(270)

#c score board
p_score = Turtle()
p_score.color("white")
p_score.penup()
p_score.hideturtle()
p_score.goto(x=-40, y=180)
p_score.setheading(270)

#paddle need to be within
game_on = True
while game_on:
    screen.update()
    time.sleep(0.05)
    comp.forward(10)
    p_score.clear()
    p_score.write(f"{ball.playerscore}", False, "center", FONT)
    c_score.clear()
    c_score.write(f"{ball.compscore}", False, "center", FONT)
    comp.auto_move()
    ball.ball_move()
    if not ball.distance(comp) > 40 or not ball.distance(player) > 40:
        if 0 < ball.heading() < 180:
            ball.setheading(180 - ball.heading())
        else:
            ball.setheading(540 - ball.heading())
        ball.forward(20)

    ball.ball_miss_paddle()







screen.exitonclick()