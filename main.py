import turtle as t
from player1 import Player1
from ball import Ball
from scoreboard import Score
import time
speed = 0.1
from player2 import Player2
screen = t.Screen()
screen.tracer(0)
screen.setup(800, 600)
screen.bgcolor("black")
player = Player1((380,0))
player2 = Player1((-390, 0))
ball = Ball()
score = Score()
screen.listen()
screen.onkey(fun=player.up, key="Up")
screen.onkey(fun=player.down, key="Down")
screen.onkey(fun=player2.up, key="w")
screen.onkey(fun=player2.down, key="s")
turtle = t.Turtle()
turtle.pensize(7)
turtle.color("white")
turtle.setheading(90)
turtle.speed(10)

turtle.goto(0,-300)
turtle.clear()
for a in range(20):

    turtle.forward(10)
    turtle.penup()
    turtle.forward(30)
    turtle.pendown()
    turtle.forward(10)


game = True
while game:
    score.clear()
    score.player2()
    score.player1()
    time.sleep(speed)
    screen.update()
    ball.bounce_l()
    if ball.ycor() < -280 or ball.ycor() > 280:
        ball.bounceY()
    if ball.distance(player.turtle) < 50 and ball.xcor() > 320 or ball.distance(player2.turtle) < 50 and ball.xcor() < -320:
        speed -= 0.002
        ball.bounceX()
    if ball.xcor() > 380:
           speed = 0.1
           score.score_2+=1

           ball.resetbounce()
           ball.bounceX()
    if ball.xcor() < -380:
       score.score_1+=1
       speed = 0.1
       ball.resetbounce()
       ball.bounceY()
       ball.bounceX()





screen.exitonclick()