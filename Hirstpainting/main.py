# import colorgram as cg
#
# color_list = cg.extract("hm.jpg", 30)
#
# color_set = []
# for color in color_list:
#     r = color.rgb[0]
#     g = color.rgb[1]
#     b = color.rgb[2]
#     rgb = (r, g, b)
#     color_set.append(rgb)
# print(color_set)
# print(color_set[0])
# print(color_set[0].r) #accessing items via method namedtuple from collections module

import turtle as t
import random
t.colormode(255)
color_list = [(198, 13, 32), (248, 236, 25), (40, 76, 188), (244, 247, 253), (39, 216, 69), (238, 227, 5), (227, 159, 49), (29, 40, 154), (212, 76, 15), (17, 153, 17), (241, 36, 161), (195, 16, 12), (223, 21, 120), (68, 10, 31), (61, 15, 8), (223, 141, 206), (11, 97, 62), (219, 159, 11), (54, 209, 229), (19, 21, 49), (238, 157, 216), (79, 74, 212), (10, 228, 238), (73, 212, 168), (93, 233, 198), (65, 231, 239), (217, 88, 51)]

tim = t.Turtle()
tim.hideturtle()
tim.speed(10)
y_coordinate = -212.13

tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
print(tim.position())

def turtle_draw():
    for a in range(10):
        tim.dot(20, random.choice(color_list))
        tim.forward(50)

def teleportation():
    tim.teleport(-212.13, y_coordinate)
    tim.setheading(0)

dot_row = 0
while dot_row < 10:
    turtle_draw()
    y_coordinate += 50
    teleportation()
    dot_row += 1

screen = t.Screen()
screen.exitonclick()