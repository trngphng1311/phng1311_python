# import DAY18
# import colorgram
#
# color_list = []
# #Extract color from the picture
# colors = colorgram.extract('DAY18.png', 20)
#
# #Return color objects
# for tone in colors:
#     r = tone.rgb.r
#     g = tone.rgb.g
#     b = tone.rgb.b
#     new_format = (r, g, b)
#     color_list.append(new_format)
#
# print(color_list)
import turtle, random
from turtle import Turtle, Screen
color_list = [(254, 254, 254), (225, 219, 221), (185, 169, 145), (139, 18, 46), (134, 173, 196), (224, 234, 227), (56, 88, 127), (215, 225, 232), (61, 27, 17), (183, 90, 103), (188, 138, 158), (169, 206, 173), (128, 187, 143), (17, 37, 68), (140, 87, 46), (219, 182, 169), (161, 201, 218), (157, 50, 82), (85, 155, 90), (217, 175, 188)]

rabow = Turtle()
turtle.colormode(255)
rabow.pensize(5)
y = float(0)

def color_u():
    color_number = random.randint(0,20)
    colorss = color_list[color_number]
    return colorss

# def random_color():
#     for step in range(10):
#         rabow.color(color_u())
#         rabow.dot(20, color_u())
#         rabow.penup()
#         rabow.forward(50)
#         rabow.pendown()
#         rabow.left(90)
#         rabow.forward(50)
#         rabow.left(90)
#         rabow.forward(500)
#
#
#
#
#
#
# random_color()

for step in range(1,100):
    rabow.dot(20, random.choice(color_list))
    rabow.penup()
    rabow.forward(50)
    if step % 10 == 0:
        rabow.setheading(90)
        rabow.forward(50)
        rabow.setheading(180)
        rabow.forward(500)
        rabow.setheading(0)


screen = Screen()
screen.exitonclick()
