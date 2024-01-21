from turtle import Turtle
from food import Food

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

food = Food()

class Snake:
    def __init__(self):
        # TODO:1 Create a snake body
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle(shape="square")
            new_segment.penup()
            new_segment.color("white")
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        # TODO:2 Move the snake
        for segment_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment_num - 1].xcor()
            new_y = self.segments[segment_num - 1].ycor()
            self.segments[segment_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)
        self.snake_eat_food()

    # TODO:3 Control the snake

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)

    # TODO:4 Check is game over
    def is_game_over(self):
        if abs(self.head.xcor()) > 300 or abs(self.head.ycor()) > 300:
            return True
        else:
            return False
        
    def snake_eat_food(self):
        
        if abs(self.head.xcor() - food.food.xcor()) <= 20 or abs(self.head.ycor() - food.food.ycor()) <= 20:
            print("Snake ate food")
            print(abs(self.head.xcor() - food.food.xcor()),abs(self.head.ycor() - food.food.ycor()))
            # Make new food
            food.make_random_food()
            # Add new segment to the snake
            self.add_segment()
    
    def add_segment(self):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        last_segment_x_cor = self.segments[-1].xcor()
        last_segment_y_cor = self.segments[-1].ycor()
        new_segment.goto(x=last_segment_x_cor, y=last_segment_y_cor)
        self.segments.append(new_segment)
