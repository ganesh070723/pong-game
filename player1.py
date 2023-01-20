from turtle import Turtle,Screen


class Player1:

    def __init__(self,position):
        self.turtle = Turtle()
        self.turtle .shape("square")
        self.turtle.color("white")
        self.turtle.penup()
        self.turtle .speed(10)
        self.turtle.goto(position)
        self.turtle.shapesize(7, 1)


    def up(self):
     if self.turtle.ycor() < 230:
        self.newy = self.turtle.ycor()+20
        self.turtle.goto(self.turtle.xcor(), self.newy)

    def down(self):
     if self.turtle.ycor() > -230:
        self.newy = self.turtle.ycor()-20
        self.turtle.goto(self.turtle.xcor(), self.newy)
