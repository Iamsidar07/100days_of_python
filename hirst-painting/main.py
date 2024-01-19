import random

# import colorgram
import turtle as t

tim = t.Turtle()
t.colormode(255)
tim.penup()
tim.hideturtle()
# colors = colorgram.extract("image.jpeg", 6)
#
# rgb_colors = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r, g, b))
#
# print(rgb_colors)

color_list = [
    (211, 210, 210),
    (189, 167, 121),
    (57, 90, 111),
    (113, 43, 35),
    (163, 89, 64),
    (210, 212, 214),
]


# def draw_row():
#     for _ in range(10):
#         random_color = random.choice(color_list)
#         tim.dot(20, random_color)
#         # tim.penup()
#         tim.forward(50)
#
#
# for row in range(1, 11):
#     draw_row()
#     tim.sety(row * 50)
#     tim.setx(0)

tim.setheading(220)

tim.forward(300)
tim.setheading(0)
num_of_dotes = 100
tim.speed("fastest")
for num_count in range(1, num_of_dotes + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if num_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = t.Screen()
screen.exitonclick()
