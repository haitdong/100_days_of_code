from turtle import Turtle

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 500
PADDLEL = 80
PADDLEW = 20
PADDLE_SPEED = 30
class Comp(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.setheading(90)
        self.penup()
        self.goto(x=480, y=0)

    def auto_move(self):
        if not SCREEN_HEIGHT / 2 - PADDLEL / 2 >= self.ycor() >= PADDLEL / 2 - SCREEN_HEIGHT / 2:
            if self.heading() == 90:
                self.setheading(270)
            elif self.heading() == 270:
                self.setheading(90)

class Player(Comp):
    def __init__(self):
        super().__init__()
        self.goto(x=-480, y=0)

    def move_up(self):
        if not self.ycor() >= SCREEN_HEIGHT / 2 - PADDLEL / 2:
            self.forward(PADDLE_SPEED)
        else:
            pass
    def move_down(self):
        if not self.ycor() <= PADDLEL / 2 - SCREEN_HEIGHT / 2:
            self.backward(PADDLE_SPEED)
        else:
            pass

