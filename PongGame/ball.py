from turtle import Turtle
import random

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 500
BALL_DIMENSION = 20
BALL_SPEED = 10
BALL_ANGLE = [160, -160, 30, -30]

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.setheading(random.choice(BALL_ANGLE))
        self.penup()
        self.playerscore = 0
        self.compscore = 0

    def ball_move(self):
        self.forward(BALL_SPEED)
        if not SCREEN_HEIGHT / 2 - BALL_DIMENSION / 2 >= self.ycor() >= BALL_DIMENSION / 2 - SCREEN_HEIGHT / 2:
            if 0 < self.heading() < 180:
                self.setheading(0 - self.heading())
            else:
                self.setheading(360-self.heading())
            self.forward(BALL_SPEED)

    def ball_miss_paddle(self):
        if self.xcor() > 500:
            print("Player Score!")
            self.home()
            self.setheading(random.choice(BALL_ANGLE))
            self.playerscore += 1
        if self.xcor() < -500:
            print("PC Score!")
            self.home()
            self.setheading(random.choice(BALL_ANGLE))
            self.compscore += 1
