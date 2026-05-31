from turtle import Screen, Turtle
import random
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)
paddle = Paddle(350, 0)
paddle2 = Paddle(-350, 0)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(paddle.up, "Up")
screen.onkeypress(paddle.down, "Down")
screen.onkeypress(paddle2.up, "w")
screen.onkeypress(paddle2.down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()   
    
    ball.move()
    
    # Detect collision with wall
    if ball.ycor() < -280 or ball.ycor() > 280:
        ball.bounce()
    
    # Detect collision with paddle
    if ball.distance(paddle) < 50 and ball.xcor() > 320 or ball.distance(paddle2) < 50 and ball.xcor() < -320:
        ball.bounce_sideways()
        ball.increase_speed()
    
    # Detect when ball goes out of bounds
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.increase_left_score()
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.increase_right_score()
    
    

















screen.exitonclick()