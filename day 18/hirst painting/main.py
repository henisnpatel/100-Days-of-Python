import colorgram
import turtle as t
import random

t.colormode(255)

screen = t.Screen()
screen.setup(width=800, height=800)

tim = t.Turtle()
tim.speed("fastest")

# colors = colorgram.extract("image.jpg", 30)
# color_list = []

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     color_list.append(new_color)
    
# print(color_list)

colorlist = [(144, 76, 50), (188, 165, 117), (248, 244, 246), (166, 153, 36), (14, 46, 85), (139, 185, 176), (146, 56, 81), (42, 110, 136), (59, 120, 99), (145, 170, 177), (87, 35, 30), (64, 152, 169), (220, 209, 93), (110, 37, 31), (100, 145, 111), (165, 99, 131), (91, 122, 172), (158, 138, 158), (177, 104, 82), (55, 52, 85), (206, 182, 195), (68, 48, 63), (73, 51, 71), (173, 201, 194), (175, 198, 201), (213, 182, 176), (37, 47, 45)]



tim.penup()
tim.setposition(-360, -360)
tim.pendown()


for _ in range(1, 101):
    tim.dot(20, random.choice(colorlist))
    tim.penup()
    tim.forward(80)
    tim.pendown()
    if _  % 10 == 0:
        tim.penup()
        tim.setposition(-360, tim.ycor() + 80)
        tim.pendown()
    

screen.exitonclick()