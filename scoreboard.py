from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("Indianred")
        self.penup()
        self.hideturtle()
        self.score_1 = 0
        self.score_2 = 0

    def player1(self):
        self.goto(100, 260)
        self.write(f"SCORE :{self.score_1}",align="center",font=("Courier", 20, "normal"))

    def player2(self):
        self.goto(-100, 260)
        self.write(f"SCORE :{self.score_2}", align="center", font=("Courier", 20, "normal"))