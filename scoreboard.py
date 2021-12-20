from turtle import Turtle

FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 260)
        self.write_current_level()

    def increase_level(self):
        self.level += 1
        self.write_current_level()

    def write_current_level(self):
        self.clear()
        self.write(f"Level: {self.level}", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", align="center", font=FONT)
