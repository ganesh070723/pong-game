
from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("SkyBlue")
        self.shapesize(1.0, 1.0)
        self.penup()
        self.xball = 10
        self.yball = 10
    def bounce_l(self):
        new_x=self.xcor()+self.xball
        new_y=self.ycor()+self.yball
        self.goto(new_x,new_y)

    def bounceY(self):
        self.yball*=-1
    def bounceX(self):
        self.xball *=-1
    def resetbounce(self):
        self.goto(0,0)

