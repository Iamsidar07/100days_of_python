from turtle import Turtle
import random
COLOR = "blue"
SHAPE = "circle"
class Food:
    # TODO: Put random food
    def __init__(self):
        self.food = Turtle(shape=SHAPE)
        self.food.penup()
        self.food.color(COLOR)
        
    def make_random_food(self):
        self.food.setx(random.randint(-270,270))
        self.food.sety(random.randint(-270,270))
