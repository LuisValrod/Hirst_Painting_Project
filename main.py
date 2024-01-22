# import colorgram
# colors = colorgram.extract('painting.jpg', 30)
#
# color_list = []
# for n in range(len(colors)):
#     r, g, b = colors[n].rgb
#     my_tuple = r, g, b
#     color_list.append(my_tuple)
# print(color_list)
import turtle
from turtle import Turtle, Screen
from random import choice
import math

# Find out initial position of the turtle.
# I want it to be from the point (0,0) 250 steps South/West direction. Same number of steps South and West
angle_in_radians = math.radians(225)
steps = 250
wPosition = math.sin(angle_in_radians) * steps
sPosition = math.cos(angle_in_radians) * steps

turtle.colormode(255)
color_list = [(244, 235, 48), (196, 12, 35), (218, 160, 70), (43, 80, 177), (237, 40, 140),
              (38, 215, 76), (237, 228, 5), (31, 40, 154), (206, 72, 22), (21, 149, 23), (201, 34, 98),
              (70, 11, 27), (182, 16, 11), (213, 164, 10), (218, 140, 195), (56, 15, 10), (17, 20, 48),
              (13, 95, 62), (79, 210, 159), (73, 73, 221), (83, 191, 220), (237, 158, 216), (94, 232, 200),
              (217, 82, 51), (5, 230, 239), (14, 64, 44)]

tim = Turtle()
screen = Screen()
y_pos = sPosition
tim.up()
tim.hideturtle()


def draw_line():
    for r in range(10):
        tim.dot(20, choice(color_list))
        tim.forward(50)


for c in range(10):
    tim.teleport(wPosition, y_pos)
    draw_line()
    y_pos += 50

screen.exitonclick()
