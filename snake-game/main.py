import time
from turtle import Turtle, Screen
from snake import Snake
import random
from food import Food

screen = Screen()
screen.setup(width=600, height=600)
screen.title("My Snake Game")
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

food.make_random_food()


is_game_on = True
while not snake.is_game_over():
    screen.update()
    time.sleep(0.1)
    snake.move()


screen.exitonclick()
