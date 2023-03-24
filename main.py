from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreBoard import Scoreboard
import time

screen = Screen()
screen.title("Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.listen()
screen.tracer(0)

scoreboard = Scoreboard()

player_pos = (-350, 0)
enemy_pos = (350, 0)

l_paddle = Paddle(player_pos)
r_paddle = Paddle(enemy_pos)
ball = Ball()

screen.onkey(fun=l_paddle.up, key="w")
screen.onkey(fun=l_paddle.down, key="s")

screen.onkey(fun=r_paddle.up, key="Up")
screen.onkey(fun=r_paddle.down, key="Down")

y_value = 10
game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move(y_value)

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    # Detect off bounds R
    if ball.xcor() > 400:
        scoreboard.l_point()
        ball.reset_pos()

    # Detect off bounds L
    if ball.xcor() < -400:
        scoreboard.r_point()
        ball.reset_pos()

screen.exitonclick()
