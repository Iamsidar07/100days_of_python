import random

# from turtle import
import turtle as t

tim = t.Turtle()

t.colormode(255)

tim.shape("turtle")
tim.speed("fastest")
# tim.color("red")
# for _ in range(4):
#     tim.forward(100)
#     tim.left(90)
# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)
# draw dashed line
# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()
colors = ["red", "orange", "yellow", "green", "brown", "yellow"]


#
#
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
#
#
# for shape_side in range(3, 11):
#     random_color = random.choice(colors)
#     tim.color(random_color)
#     draw_shape(shape_side)
# directions = [0, 90, 180, 270]


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


# tim.forward(100)
# for _ in range(200):
#     color = random_color()
#     tim.color(color)
#     tim.pensize(random.randint(9, 15))
#     tim.speed(random.randint(4, 9))
#     tim.forward(30)
#     tim.setheading(random.choice(directions))


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(10)

screen = t.Screen()
screen.exitonclick()
