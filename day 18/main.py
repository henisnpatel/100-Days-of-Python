from turtle import Turtle, Screen
import random 
import turtle as t

t.colormode(255)

tim = Turtle()

tim.shape("turtle")


tim.pensize(1)
tim.speed("fastest")

def spirograph(size_of_gap):
    for _ in range(360 // size_of_gap):
        tim.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        tim.circle(100)
        tim.left(size_of_gap)


spirograph(10)
        

















screen = Screen()
screen.exitonclick()