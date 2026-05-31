from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260) 
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"{self.left_score} : {self.right_score}", align="center", font=("Courier", 30, "normal"))

    def increase_left_score(self):
        self.left_score += 1
        self.update_scoreboard()
    
    def increase_right_score(self):
        self.right_score += 1
        self.update_scoreboard()
