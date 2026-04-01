from turtle import Turtle

class Score(Turtle):
    def __init__(self, xcor, ycor):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(x=xcor, y=ycor)
        self.setheading(270)

    def dash_line(self):
        for a in range(13):
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)
            self.pendown()