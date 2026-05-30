from random import random, randint
from turtle import Turtle, Screen


is_true = False

screen = Screen()
screen.setup(width=500, height=400)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

userbet = screen.textinput(title="Hello", prompt="Which colour do you want to choose? ")

for i in range(6):
    tim = Turtle(shape="turtle")
    tim.color(colors[i])
    tim.penup()
    tim.goto(-230, y=-100 + (i * 40))
    all_turtles.append(tim)

if userbet:
    is_true = True
    while is_true:
        for tim in all_turtles:
            ran_distance = randint(0, 15)
            tim.forward(ran_distance)
            if tim.xcor() > 230:
                is_true = False
                winner = tim.pencolor()
                if winner == userbet:
                    print(f"You win! The {winner} turtle is the winner!")
                else:
                    print(f"You lose! The {winner} turtle is the winner!")
                exit()

screen.exitonclick()