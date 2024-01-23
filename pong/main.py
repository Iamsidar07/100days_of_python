import time
from turtle import Screen

from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

# TODO: 1 Create the screen
screen = Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(fun=r_paddle.move_up, key="Up")
screen.onkey(fun=r_paddle.move_down, key="Down")
screen.onkey(fun=l_paddle.move_up, key="w")
screen.onkey(fun=l_paddle.move_down, key="s")
is_game_on = True
while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #     Detect collision with wall
    if abs(ball.ycor()) > 280:
        ball.bounce_y()

    #     Detect collision with paddle
    if (
        ball.distance(r_paddle) < 50
        or ball.distance(l_paddle) < 50
        and abs(ball.xcor()) > 320
    ):
        ball.bounce_x()

    #     Detect when paddle misses
    if ball.xcor() > 390:
        #         right paddle misses
        ball.reset_position()
        #         Increase score for left paddle
        scoreboard.increase_l_score()

    if ball.xcor() < -390:
        ball.reset_position()
        #         Increase score for right paddle
        scoreboard.increase_r_score()


screen.exitonclick()
