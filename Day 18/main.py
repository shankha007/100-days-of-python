import turtle as t
import random

# Extracted using colorgram.py
colors_list = [(84, 254, 155), (173, 146, 118), (245, 39, 191), (158, 107, 56), (2, 1, 176), (151, 54, 251), (221, 254, 101), (253, 146, 193), (3, 87, 176), (249, 1, 246), (35, 34, 253), (1, 213, 212), (249, 0, 0), (254, 147, 146), (253, 71, 70), (39, 249, 42), (85, 249, 253), (240, 1, 13), (5, 210, 216), (230, 126, 190), (2, 2, 107), (135, 152, 220), (174, 162, 249), (208, 118, 26), (253, 7, 4), (248, 6, 19)]

t.colormode(255)
tim = t.Turtle()
screen = t.Screen()

height = screen.screensize()[0]
width = screen.screensize()[1]

tim.speed("fastest")
tim.penup()
tim.hideturtle()

initial_x = -height + 50
initial_y = -width + 50
tim.goto(initial_x, initial_y)

for i in range(10):
    tim.setx(initial_x)
    tim.sety(initial_y + i * 50)
    for j in range(10):
        tim.pendown()
        tim.dot(20, random.choice(colors_list))
        tim.penup()
        tim.setx(tim.pos()[0] + 50)

screen.exitonclick()