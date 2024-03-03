import turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 1

    def display_level(self):
        self.clear()
        self.goto(-280, 250)
        self.write(arg=f"Level:{self.level}", align="left", font=FONT)

    def update_level(self):
        self.level += 1

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER!!", align="center", font=FONT)