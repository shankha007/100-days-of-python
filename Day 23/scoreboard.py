from turtle import Turtle

FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("black")
        self.penup()
        self.goto(-280, 250)
        self.level = 1
        self.refresh_scoreboard()

    def refresh_scoreboard(self):
        self.clear()
        self.write(f"Level {self.level}", align="left", font=FONT)

    def increase_score(self):
        self.level += 1
        self.refresh_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)