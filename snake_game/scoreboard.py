from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.teleport(x=0, y=260)
        self.score = 0
        self.high_score = 0
        self.current_highscore = 0
        self.scoreboard()

    def scoreboard(self):
        with open("../../../OneDrive/Desktop/data.txt") as d:
            self.current_highscore = d.read()
        self.write(f"Score: {self.score}  High Score: {self.current_highscore}", move=False, align="center", font=(FONT))

    def score_increase(self):
        self.score += 1
        self.clear()
        self.scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("../../../OneDrive/Desktop/data.txt", "w") as d:
                d.write(f"{self.high_score}")
        self.score = 0
        self.clear()
        self.scoreboard()