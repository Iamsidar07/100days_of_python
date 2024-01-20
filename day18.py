# Event listeners
from turtle import Turtle, Screen

tim = Turtle()


def move_forward():
    tim.forward(20)


def move_backward():
    tim.backward(20)


def turn_left():
    new_heading = tim.heading() + 20
    tim.setheading(new_heading)


def turn_right():
    new_heading = tim.heading() - 20
    tim.setheading(new_heading)


def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen = Screen()
screen.listen()

# screen.onkey(fun=move_forward, key="space")

screen.onkey(fun=move_forward, key="w")
screen.onkey(fun=move_backward, key="s")
screen.onkey(fun=turn_right, key="d")
screen.onkey(fun=turn_left, key="a")
screen.onkey(fun=clear_screen, key="c")
screen.exitonclick()
